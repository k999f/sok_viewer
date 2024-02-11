import sys
import pandas as pd
import pyqtgraph as pg
import pyqtgraph.exporters
from copy import deepcopy
from datetime import timedelta
import time


from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QCheckBox, QVBoxLayout, QListWidgetItem, QColorDialog
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QCursor, QColor

from ui_form import Ui_Widget

# Название столбца со значениями времени
timeParameter = "NVG_timeLoc"

# Класс Widget – основное окно приложения, внутри которого находятся другие элементы интерфейса
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Создаем объект ui, внутри которого находятся элементы интерфейса, описанные в ui_form.py
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # data – DataFrame, в котором хранятся данные из файла
        # selectedParameters – параметры, отображаемые на графике
        # time – список со значениями времени
        # fileAlreadyOpened - был ли ранее открыт файл 
        # plotPointerX, plotPointerY - координаты указателя
        # plotGrid, plotBackgroundColor, plotZoomMode - параметры графика: сетка, цвет фона, режим работы (X, XY, область)
        # legendScale - масштаб подписей для обозначений цветов графиков
        # layersNumber - количество слоев
        # currentLayer - текущий слой
        # layersParameters - список с параметрами слоев 
        self.data = pd.DataFrame() 
        self.selectedParameters = list()
        self.time = list()
        self.fileAlreadyOpened = False
        self.plotPointerX = str()
        self.plotPointerY = str()
        self.plotGrid = False
        self.plotBackgroundColor = "Black"
        self.plotZoomMode = "XY"
        self.legendScale = 1
        self.layersNumber = 5
        self.currentLayer = 0
        self.layersParameters = list()

    # Обработка события нажатия на кнопку "Файл" (кнопка открытия файла)
    def dataButtonClicked(self):
        options = QFileDialog.Options()
        # Получаем имя выбранного файла в формате .csv
        fileName, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "CSV files (*.csv)", options=options)
        # Если файл выбран
        if fileName:
            # Пытаемся выполнить следующие действия
            try:
                # print("Файл \"" + fileName.split("/")[-1] + "\" загружается")

                # Читаем файл, удаляем строки с повторяющимися значениями времени
                # время записываем в отдельный список
                self.data = pd.read_csv(fileName, sep=';')
                self.data.drop_duplicates(subset=timeParameter, inplace=True)
                self.time = list(self.data[timeParameter])
                self.data.drop(columns=[timeParameter], axis=1, inplace=True)

                # Формируем список словарей для слоев, в каждом из которых хранится: номер слоя, выбранные параметры,
                # список объектов QCheckBox, координаты X и Y для указателя
                for i in range(self.layersNumber):
                    dictionary = {"number": i,
                                  "parameters": list(), "checkBoxes": list(), "pointerX": str(), "pointerY": str()}
                    self.layersParameters.append(dictionary)

                # Если файл открыт впервые после запуска программы
                if not self.fileAlreadyOpened:
                    # Создаем временную ось
                    dateAxis = pg.graphicsItems.DateAxisItem.DateAxisItem(
                        orientation='bottom', utcOffset=0)
                    # Создаем виджет для отображения графиков
                    self.plotWidget = pg.PlotWidget(
                        axisItems={'bottom': dateAxis})
                    self.plotWidget.setObjectName(u"plotWidget")
                    # Привязываем функцию plotClicked к событию нажатия на график
                    self.plotWidget.scene().sigMouseClicked.connect(self.plotClicked)
                    self.plotWidget.setCursor(QCursor(Qt.CrossCursor))

                    # Отключаем дефолтные элементы управления графиком
                    self.plotWidget.plotItem.setMenuEnabled(False)
                    self.plotWidget.hideButtons()

                    # Устанавливаем диапазон значений по оси X
                    startTime = self.time[0]
                    endTime = self.time[len(self.time) - 1]
                    self.plotWidget.setXRange(startTime, endTime)
                    ax = self.plotWidget.getAxis('bottom')

                    # Задаем отступ в 10 процентов от левой и правой границы графика
                    xMargin = (endTime - startTime) * 0.1
                    self.plotWidget.plotItem.vb.setLimits(
                        xMin=startTime - xMargin, xMax=endTime + xMargin, minXRange=3)

                    self.ui.plotLayout.addWidget(self.plotWidget)

                    # Создаем список параметров в окне "Параметры"
                    createParametersList()

                    self.ui.layersWidget.setEnabled(True)

                    self.fileAlreadyOpened = True
                # Если в программе после запуска уже открывался какой-либо файл
                else:
                    # Очищаем все данные
                    self.selectedParameters.clear()

                    self.plotWidget.clear()

                    self.plotPointerX = str()
                    self.plotPointerY = str()

                    self.ui.valuesListWidget.clear()

                    self.ui.exportButton.setEnabled(False)

                    createParametersList()

                    self.ui.layersWidget.setEnabled(True)

                # Устанавливаем область обзора для всех слоев по умолчанию
                defaultViewRange = self.plotWidget.plotItem.vb.viewRect()
                for i in range(self.layersNumber):
                    self.layersParameters[i]["viewRange"] = defaultViewRange

                setPlotParameters()
                fileAlreadyOpened = True
                self.ui.fileStatusLabel.clear()

                # print("Файл \"" + fileName.split("/")[-1] + "\" загружен")

            # Если какое-то из описанных выше действий завершилось неудачно 
            # (обычно это происходит когда файл имеет неправильный формат)
            except:
                # Очищаем все данные
                if len(self.selectedParameters) != 0:
                    self.plotWidget.clear()

                self.layersParameters.clear()
                self.currentLayer = 0

                self.data = pd.DataFrame()
                self.time = list()
                self.selectedParameters.clear()

                self.plotPointerX = str()
                self.plotPointerY = str()

                self.ui.valuesListWidget.clear()

                self.ui.exportButton.setEnabled(False)
                self.ui.layersWidget.setEnabled(False)
                self.ui.layersWidget.setCurrentIndex(0)

                createParametersList()

                # Выводим в окне сообщение об ошибке
                self.ui.fileStatusLabel.setText("Ошибка открытия файла")
                self.ui.fileStatusLabel.setStyleSheet("color: rgb(255, 0, 0); font-size: 11px;")

                # print("Ошибка открытия файла \"" + fileName.split("/")[-1])

    # Обработка смены слоя
    def layerChanged(self, newLayer):
        # Делаем активной кнопку выбранного нового слоя
        self.ui.layersWidget.setCurrentIndex(newLayer)
        selectedCheckBoxes = list()
        # Копируем данные из предыдущего слоя
        selectedParameters = deepcopy(self.selectedParameters)
        plotPointerX = deepcopy(self.plotPointerX)
        plotPointerY = deepcopy(self.plotPointerY)
        viewRange = self.plotWidget.plotItem.vb.viewRect()

        # Копируем и отключаем чекбоксы для предыдущего слоя
        for checkBox in self.ui.parametersScrollArea.findChildren(QCheckBox):
            if checkBox.isChecked():
                selectedCheckBoxes.append(checkBox)
                checkBox.setCheckState(Qt.Unchecked)

        # Формируем словарь с данными для предыдущего слоя и заносим его в список параметров для слоев
        dictionary = {"number": self.currentLayer,
                      "parameters": selectedParameters, "checkBoxes": selectedCheckBoxes, "pointerX": plotPointerX, "pointerY": plotPointerY, "viewRange": viewRange}
        self.layersParameters[self.currentLayer] = dictionary

        # Меняем номер текущего слоя
        self.currentLayer = newLayer
        # Устанавливаем новые параметры для текущего слоя
        self.selectedParameters = self.layersParameters[newLayer]["parameters"]
        self.plotPointerX = self.layersParameters[newLayer]["pointerX"]
        self.plotPointerY = self.layersParameters[newLayer]["pointerY"]
        self.plotWidget.plotItem.vb.setRange(
            self.layersParameters[newLayer]["viewRange"], padding=0)

        # Активируем чекбоксы для текущего слоя
        for checkBox in self.layersParameters[newLayer]["checkBoxes"]:
            checkBox.setCheckState(Qt.Checked)

        # Перерисовываем график, если для выбранного слоя активированы какие-либо параметры
        if len(self.layersParameters[newLayer]["checkBoxes"]) == 0:
            drawPlot()

    # Обработка нажатия на кнопку "Экспорт"
    def exportButtonClicked(self):
        # Получаем имя экспортируемого файла
        exportFileName, _ = QFileDialog.getSaveFileName(
            self, 'Экспортировать график')
        # Если имя получено, сохраняем график в формате .png
        if exportFileName:
            self.legendScale = 4
            drawPlot()
            exporter = pg.exporters.ImageExporter(self.plotWidget.scene())
            exporter.parameters()['width'] = 3000
            exporter.export(exportFileName + ".png")
            self.legendScale = 1
            drawPlot()

    # Обработка нажатия на чекбокс
    def checkBoxStateChanged(self, objectName, checkBox):
        def stateChanged(state):
            if state == 2:
                addParameter(objectName, checkBox)
            elif state == 0:
                deleteParameter(objectName, checkBox)
        return stateChanged

    # Обработка нажатия на график
    def plotClicked(self, mouseEvent):
        # Если нажата ЛКМ
        if mouseEvent.button() == Qt.LeftButton:
            # Если для текущего слоя автивны какие-либо параметры
            if self.selectedParameters:
                # Получаем координаты указателя и записываем их в plotPointerX и plotPointerY
                viewBox = self.plotWidget.plotItem.vb
                sceneCoords = mouseEvent.scenePos()
                if self.plotWidget.sceneBoundingRect().contains(sceneCoords):
                    mousePoint = viewBox.mapSceneToView(sceneCoords)
                    startTime = self.time[0]
                    endTime = self.time[len(self.time) - 1]
                    if mousePoint.x() >= startTime and mousePoint.x() <= endTime:
                        self.plotPointerX = mousePoint.x()
                        self.plotPointerY = mousePoint.y()

                        # В окне "Значения" отображаем значения параметров для установленного указателя 
                        createValuesList()

                    drawPlot()
        # Если нажата ПКМ, очищаем координаты указателя
        elif mouseEvent.button() == Qt.RightButton:
            self.plotPointerX = str()
            self.plotPointerY = str()
            drawPlot()

    # Обработка изменения режима работы с графиком
    def zoomModeChanged(self, checked):
        if not checked:
            return

        # Устанавливаем режим графика в зависимости от выбранного пункта
        if self.ui.radioButtonX.isChecked():
            self.plotZoomMode = "X"
        elif self.ui.radioButtonY.isChecked():
            self.plotZoomMode = "Y"
        elif self.ui.radioButtonXY.isChecked():
            self.plotZoomMode = "XY"
        elif self.ui.radioButtonArea.isChecked():
            self.plotZoomMode = "Area"

        if self.fileAlreadyOpened:
            drawPlot()

    # Обработка изменения режима работы с графиком
    def backgroundChanged(self, checked):
        if not checked:
            return

        # Устанавливаем цвет графика в зависимости от выбранного пункта
        if self.ui.blackRadioButton.isChecked():
            self.plotBackgroundColor = "Black"
        elif self.ui.whiteRadioButton.isChecked():
            self.plotBackgroundColor = "White"

        if self.fileAlreadyOpened:
            drawPlot()

    # Обработка нажатия на кнопку автозума
    def autozoomClicked(self):
        if len(self.selectedParameters) != 0:
            self.plotWidget.autoRange()

    # Обработка нажатия на чекбокс сетки
    def gridClicked(self, state):
        if state == 2:
            self.plotGrid = True
        elif state == 0:
            self.plotGrid = False

        if self.fileAlreadyOpened:
            drawPlot()


# Создание списка значений параметров для установленного указателя в окне "Значения"
def createValuesList():
    if widget.plotPointerX and widget.plotPointerY:
        time = list(widget.time)
        pointerTime = round(widget.plotPointerX)
        widget.ui.valuesListWidget.clear()
        # Если указатель установлен в временной точке, для которой в файле существет значение
        try:
            index = time.index(pointerTime)
            for parameter in widget.selectedParameters:
                name = parameter["name"]
                value = str(list(parameter["data"])[index])
                color = parameter["color"]

                item = QListWidgetItem(name + " = " + value)
                textColor = pg.mkColor(color)
                item.setForeground(textColor)
                widget.ui.valuesListWidget.addItem(item)
        # Если указатель установлен в временной точке, для которой в файле не существет значения,
        # то значения параметров равны 0
        except ValueError:
            for parameter in widget.selectedParameters:
                name = parameter["name"]
                value = "0"
                color = parameter["color"]

                item = QListWidgetItem(name + " = " + value)
                textColor = pg.mkColor(color)
                item.setForeground(textColor)
                widget.ui.valuesListWidget.addItem(item)


# Функция добавления параметра при его активации
def addParameter(name, checkBox):
    parameterAlreadySet = False
    color = QColor()

    # Проверяем, был ли выставлен параметр пользователем вручную, или повторно активируется при выборе слоя
    for parameter in widget.selectedParameters:
        if name == parameter["name"]:
            parameterAlreadySet = True
            color = parameter["color"]

    # Если параметр повторно активируется при выборе слоя
    if parameterAlreadySet:
        textColor = pg.mkColor(color)
        checkBox.setStyleSheet("color: " + textColor.name())

        # Если параметры не выбраны, делаем кнопку экспорта неактивной, иначе - активной
        if len(widget.selectedParameters) != 0:
            widget.ui.exportButton.setEnabled(True)
        else:
            widget.ui.exportButton.setEnabled(False)

        drawPlot()
        createValuesList()
    # Если параметр выбран вручную пользователем
    else:
        color = QColorDialog.getColor()
        if color.isValid():
            dictionary = {"name": name,
                          "data": widget.data[name], "color": color}
            widget.selectedParameters.append(dictionary)

            textColor = pg.mkColor(color)
            checkBox.setStyleSheet("color: " + textColor.name())

            if len(widget.selectedParameters) != 0:
                widget.ui.exportButton.setEnabled(True)
            else:
                widget.ui.exportButton.setEnabled(False)

            drawPlot()
            createValuesList()
        else:
            checkBox.setCheckState(Qt.Unchecked)


# Функция удаления параметра
def deleteParameter(name, checkBox):
    for parameter in widget.selectedParameters:
        if parameter["name"] == name:
            index = widget.selectedParameters.index(parameter)
            widget.selectedParameters.pop(index)

    checkBox.setStyleSheet("color: black")

    # Если параметры не выбраны, делаем кнопку экспорта неактивной, иначе - активной
    if len(widget.selectedParameters) != 0:
        widget.ui.exportButton.setEnabled(True)
    else:
        widget.ui.exportButton.setEnabled(False)

    drawPlot()
    createValuesList()


# Установка параметров графика: цвета, сетки, режима работы
def setPlotParameters():
    if widget.plotBackgroundColor == "White":
        widget.plotWidget.setBackground(pg.mkColor(245, 245, 245))
    elif widget.plotBackgroundColor == "Black":
        widget.plotWidget.setBackground('k')

    if widget.plotZoomMode == "XY":
        widget.plotWidget.plotItem.getViewBox().setMouseMode(pg.ViewBox.PanMode)
        widget.plotWidget.plotItem.setMouseEnabled(x=True, y=True)
    elif widget.plotZoomMode == "X":
        widget.plotWidget.plotItem.getViewBox().setMouseMode(pg.ViewBox.PanMode)
        widget.plotWidget.plotItem.setMouseEnabled(x=True, y=False)
    elif widget.plotZoomMode == "Y":
        widget.plotWidget.plotItem.getViewBox().setMouseMode(pg.ViewBox.PanMode)
        widget.plotWidget.plotItem.setMouseEnabled(x=False, y=True)
    elif widget.plotZoomMode == "Area":
        widget.plotWidget.plotItem.setMouseEnabled(x=True, y=True)
        widget.plotWidget.plotItem.getViewBox().setMouseMode(pg.ViewBox.RectMode)

    if widget.plotGrid:
        widget.plotWidget.showGrid(x=True, y=True)
    else:
        widget.plotWidget.showGrid(x=False, y=False)


# Функция отрисовки графика
def drawPlot():
    # Очищаем график
    widget.plotWidget.clear()
    setPlotParameters()
    legend = widget.plotWidget.addLegend()
    legend.setScale(widget.legendScale)

    # Добавляем на график выбранные параметры
    for parameter in widget.selectedParameters:
        widget.plotWidget.plot(
            widget.time, parameter["data"], pen=pg.mkPen(parameter["color"], width=1), name=parameter["name"])

    ax = widget.plotWidget.getAxis('bottom')

    # Если установлен указатель, отображаем его
    if widget.plotPointerX and widget.plotPointerY:
        x = widget.plotPointerX
        y = widget.plotPointerY
        if widget.plotBackgroundColor == "Black":
            pen = pg.mkPen(color=(220, 220, 220), style=Qt.DashLine)
        elif widget.plotBackgroundColor == "White":
            pen = pg.mkPen(color=(0, 0, 0), style=Qt.DashLine)
        verticalLine = pg.InfiniteLine(pos=x, angle=90, pen=pen)
        horizontalLine = pg.InfiniteLine(pos=y, angle=0, pen=pen)
        widget.plotWidget.addItem(verticalLine)
        widget.plotWidget.addItem(horizontalLine)

        # Отображаем значение времени рядом с указателем
        timeValue = str(timedelta(seconds=round(x)))
        if widget.plotBackgroundColor == "Black":
            timeText = pg.TextItem(timeValue, color=(173, 173, 173))
        elif widget.plotBackgroundColor == "White":
            timeText = pg.TextItem(timeValue, color=(0, 0, 0))
        widget.plotWidget.addItem(timeText)
        timeText.setPos(x, y)


# Функция создания значений параметров для установленного указателя (окно "Значения")
def createParametersList():
    parametersLayout = QVBoxLayout()
    for parameterName in widget.data.columns:
        checkBox = QCheckBox(parameterName, objectName=parameterName)
        checkBox.stateChanged.connect(
            widget.checkBoxStateChanged(parameterName, checkBox))
        checkBox.setCursor(QCursor(Qt.PointingHandCursor))
        parametersLayout.addWidget(checkBox)
    parametersWidget = QWidget()
    widget.setContentsMargins(0, 0, 0, 0)
    parametersWidget.setLayout(parametersLayout)
    widget.ui.parametersScrollArea.setWidget(parametersWidget)

# Зоздание и отображение окна приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
