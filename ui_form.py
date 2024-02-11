# -*- coding: utf-8 -*-

# Файл сгенерирован из form.ui
# При сборке проекта через Qt Creator все изменения, внесенные вручную, удалятся (останется только то, что описано в файле form.ui)


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1003, 601)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.valuesLabel = QLabel(Widget)
        self.valuesLabel.setObjectName(u"valuesLabel")
        self.valuesLabel.setMinimumSize(QSize(151, 16))
        self.valuesLabel.setMaximumSize(QSize(16777215, 16))
        font = QFont()
        font.setFamilies([u"Verdana"])
        self.valuesLabel.setFont(font)

        self.gridLayout.addWidget(self.valuesLabel, 1, 2, 1, 1)

        self.parametersScrollArea = QScrollArea(Widget)
        self.parametersScrollArea.setObjectName(u"parametersScrollArea")
        self.parametersScrollArea.setMinimumSize(QSize(151, 0))
        self.parametersScrollArea.setMaximumSize(QSize(151, 16777215))
        self.parametersScrollArea.setFont(font)
        self.parametersScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 149, 499))
        self.parametersScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.parametersScrollArea, 2, 0, 1, 1)

        self.plotButtonsWidget = QWidget(Widget)
        self.plotButtonsWidget.setObjectName(u"plotButtonsWidget")
        self.plotButtonsWidget.setMinimumSize(QSize(631, 20))
        self.zoomBox = QGroupBox(self.plotButtonsWidget)
        self.zoomBox.setObjectName(u"zoomBox")
        self.zoomBox.setGeometry(QRect(56, 0, 211, 20))
        self.zoomBox.setMinimumSize(QSize(145, 20))
        self.zoomBox.setMaximumSize(QSize(16777215, 16777215))
        self.zoomBox.setStyleSheet(u"font-size: 11px;")
        self.radioButtonXY = QRadioButton(self.zoomBox)
        self.radioButtonXY.setObjectName(u"radioButtonXY")
        self.radioButtonXY.setGeometry(QRect(6, 0, 49, 20))
        self.radioButtonXY.setMinimumSize(QSize(49, 20))
        self.radioButtonXY.setMaximumSize(QSize(16777215, 16777215))
        self.radioButtonXY.setFont(font)
        self.radioButtonXY.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButtonXY.setCheckable(True)
        self.radioButtonXY.setChecked(True)
        self.radioButtonX = QRadioButton(self.zoomBox)
        self.radioButtonX.setObjectName(u"radioButtonX")
        self.radioButtonX.setGeometry(QRect(59, 0, 49, 20))
        self.radioButtonX.setMinimumSize(QSize(49, 20))
        self.radioButtonX.setMaximumSize(QSize(16777215, 16777215))
        self.radioButtonX.setFont(font)
        self.radioButtonX.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButtonX.setCheckable(True)
        self.radioButtonY = QRadioButton(self.zoomBox)
        self.radioButtonY.setObjectName(u"radioButtonY")
        self.radioButtonY.setGeometry(QRect(100, 0, 49, 20))
        self.radioButtonY.setMinimumSize(QSize(49, 20))
        self.radioButtonY.setMaximumSize(QSize(16777215, 16777215))
        self.radioButtonY.setFont(font)
        self.radioButtonY.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButtonArea = QRadioButton(self.zoomBox)
        self.radioButtonArea.setObjectName(u"radioButtonArea")
        self.radioButtonArea.setGeometry(QRect(138, 0, 77, 20))
        self.radioButtonArea.setMinimumSize(QSize(77, 20))
        self.radioButtonArea.setFont(font)
        self.radioButtonArea.setCursor(QCursor(Qt.PointingHandCursor))
        self.gridCheckBox = QCheckBox(self.plotButtonsWidget)
        self.gridCheckBox.setObjectName(u"gridCheckBox")
        self.gridCheckBox.setGeometry(QRect(347, 1, 61, 20))
        self.gridCheckBox.setMinimumSize(QSize(61, 20))
        self.gridCheckBox.setMaximumSize(QSize(16777215, 16777215))
        self.gridCheckBox.setFont(font)
        self.gridCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.gridCheckBox.setStyleSheet(u"font-size: 11px;")
        self.backgroundLabel = QLabel(self.plotButtonsWidget)
        self.backgroundLabel.setObjectName(u"backgroundLabel")
        self.backgroundLabel.setGeometry(QRect(445, 2, 31, 16))
        self.backgroundLabel.setMinimumSize(QSize(31, 16))
        self.backgroundLabel.setMaximumSize(QSize(16777215, 16777215))
        self.backgroundLabel.setFont(font)
        self.backgroundLabel.setStyleSheet(u"font-size: 11px;")
        self.scaleLabel = QLabel(self.plotButtonsWidget)
        self.scaleLabel.setObjectName(u"scaleLabel")
        self.scaleLabel.setGeometry(QRect(11, 2, 45, 16))
        self.scaleLabel.setMinimumSize(QSize(45, 16))
        self.scaleLabel.setMaximumSize(QSize(16777215, 16777215))
        self.scaleLabel.setFont(font)
        self.scaleLabel.setStyleSheet(u"font-size: 11px;")
        self.backgroundBox = QGroupBox(self.plotButtonsWidget)
        self.backgroundBox.setObjectName(u"backgroundBox")
        self.backgroundBox.setGeometry(QRect(475, 0, 146, 21))
        self.backgroundBox.setMinimumSize(QSize(146, 21))
        self.backgroundBox.setMaximumSize(QSize(16777215, 16777215))
        self.backgroundBox.setStyleSheet(u"font-size: 11px;")
        self.blackRadioButton = QRadioButton(self.backgroundBox)
        self.blackRadioButton.setObjectName(u"blackRadioButton")
        self.blackRadioButton.setGeometry(QRect(8, 0, 74, 20))
        self.blackRadioButton.setMinimumSize(QSize(74, 20))
        self.blackRadioButton.setMaximumSize(QSize(16777215, 16777215))
        self.blackRadioButton.setFont(font)
        self.blackRadioButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.blackRadioButton.setChecked(True)
        self.whiteRadioButton = QRadioButton(self.backgroundBox)
        self.whiteRadioButton.setObjectName(u"whiteRadioButton")
        self.whiteRadioButton.setGeometry(QRect(80, 0, 61, 20))
        self.whiteRadioButton.setMinimumSize(QSize(61, 20))
        self.whiteRadioButton.setMaximumSize(QSize(16777215, 16777215))
        self.whiteRadioButton.setFont(font)
        self.whiteRadioButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.autozoomButton = QPushButton(self.plotButtonsWidget)
        self.autozoomButton.setObjectName(u"autozoomButton")
        self.autozoomButton.setGeometry(QRect(270, 0, 41, 20))
        self.autozoomButton.setMinimumSize(QSize(25, 20))
        self.autozoomButton.setMaximumSize(QSize(16777215, 16777215))
        self.autozoomButton.setFont(font)
        self.autozoomButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.autozoomButton.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: rgb(175, 175, 175);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(241, 241, 241);\n"
"	font-size: 11px;\n"
"}\n"
"QPushButton::pressed {\n"
"	border: 1px solid;\n"
"	border-color: rgb(175, 175, 175);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(185, 185, 185);\n"
"	font-size: 11px;\n"
"}")

        self.gridLayout.addWidget(self.plotButtonsWidget, 1, 1, 1, 1, Qt.AlignHCenter)

        self.parametersLabel = QLabel(Widget)
        self.parametersLabel.setObjectName(u"parametersLabel")
        self.parametersLabel.setMaximumSize(QSize(151, 16777215))
        self.parametersLabel.setFont(font)

        self.gridLayout.addWidget(self.parametersLabel, 1, 0, 1, 1)

        self.mainPlotWidget = QWidget(Widget)
        self.mainPlotWidget.setObjectName(u"mainPlotWidget")
        self.mainPlotWidget.setMinimumSize(QSize(647, 501))
        self.plotLayout = QVBoxLayout(self.mainPlotWidget)
        self.plotLayout.setObjectName(u"plotLayout")
        self.plotLayout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.mainPlotWidget, 2, 1, 1, 1)

        self.valuesListWidget = QListWidget(Widget)
        self.valuesListWidget.setObjectName(u"valuesListWidget")
        self.valuesListWidget.setMinimumSize(QSize(161, 501))
        self.valuesListWidget.setMaximumSize(QSize(161, 16777215))
        self.valuesListWidget.setFont(font)

        self.gridLayout.addWidget(self.valuesListWidget, 2, 2, 1, 1)

        self.controlBox = QGroupBox(Widget)
        self.controlBox.setObjectName(u"controlBox")
        self.controlBox.setMinimumSize(QSize(0, 31))
        self.controlBox.setMaximumSize(QSize(16777215, 31))
        self.controlBox.setAutoFillBackground(False)
        self.dataButton = QPushButton(self.controlBox)
        self.dataButton.setObjectName(u"dataButton")
        self.dataButton.setEnabled(True)
        self.dataButton.setGeometry(QRect(10, 3, 70, 24))
        self.dataButton.setMinimumSize(QSize(70, 24))
        self.dataButton.setMaximumSize(QSize(16777215, 16777215))
        self.dataButton.setFont(font)
        self.dataButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.dataButton.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: rgb(175, 175, 175);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(241, 241, 241);\n"
"	font-size: 13px;\n"
"}\n"
"QPushButton::pressed {\n"
"	border: 1px solid;\n"
"	border-color: rgb(175, 175, 175);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(185, 185, 185);\n"
"	font-size: 13px;\n"
"}")
        self.dataButton.setFlat(False)
        self.exportButton = QPushButton(self.controlBox)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setEnabled(False)
        self.exportButton.setGeometry(QRect(90, 3, 70, 24))
        self.exportButton.setMinimumSize(QSize(70, 24))
        self.exportButton.setFont(font)
        self.exportButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.exportButton.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: rgb(175, 175, 175);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(241, 241, 241);\n"
"	font-size: 13px;\n"
"}\n"
"QPushButton:pressed {\n"
"	border: 1px solid;\n"
"	border-color: rgb(175, 175, 175);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(185, 185, 185);\n"
"	font-size: 13px;\n"
"}")
        self.fileStatusLabel = QLabel(self.controlBox)
        self.fileStatusLabel.setObjectName(u"fileStatusLabel")
        self.fileStatusLabel.setGeometry(QRect(310, 8, 165, 16))
        self.fileStatusLabel.setMinimumSize(QSize(165, 0))
        self.fileStatusLabel.setMaximumSize(QSize(161, 16777215))
        self.fileStatusLabel.setFont(font)
        self.fileStatusLabel.setStyleSheet(u"font-size: 11px;")
        self.layersWidget = QTabWidget(self.controlBox)
        self.layersWidget.setObjectName(u"layersWidget")
        self.layersWidget.setEnabled(False)
        self.layersWidget.setGeometry(QRect(167, 3, 140, 24))
        self.layersWidget.setMinimumSize(QSize(140, 24))
        self.layersWidget.setMaximumSize(QSize(165, 24))
        self.layersWidget.setFont(font)
        self.layersWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.layersWidget.setStyleSheet(u"QTabBar::tab {\n"
"	background-color: rgb(241, 241, 241);\n"
"	border: 1px solid rgb(175, 175, 175);\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"	min-width: 20px;\n"
"	min-height: 20;\n"
"	padding: 1px;\n"
"	margin-right:2px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"	background-color: rgb(185, 185, 185);\n"
"	border-color: rgb(175, 175, 175);\n"
"}\n"
"QTabWidget::pane{\n"
"	border-bottom: 0px;\n"
"}")
        self.layer1 = QWidget()
        self.layer1.setObjectName(u"layer1")
        self.layersWidget.addTab(self.layer1, "")
        self.layer2 = QWidget()
        self.layer2.setObjectName(u"layer2")
        self.layersWidget.addTab(self.layer2, "")
        self.layer3 = QWidget()
        self.layer3.setObjectName(u"layer3")
        self.layersWidget.addTab(self.layer3, "")
        self.layer4 = QWidget()
        self.layer4.setObjectName(u"layer4")
        self.layersWidget.addTab(self.layer4, "")
        self.layer5 = QWidget()
        self.layer5.setObjectName(u"layer5")
        self.layersWidget.addTab(self.layer5, "")

        self.gridLayout.addWidget(self.controlBox, 0, 0, 1, 3)


        self.retranslateUi(Widget)
        self.dataButton.clicked.connect(Widget.dataButtonClicked)
        self.radioButtonXY.toggled.connect(Widget.zoomModeChanged)
        self.radioButtonX.toggled.connect(Widget.zoomModeChanged)
        self.radioButtonY.toggled.connect(Widget.zoomModeChanged)
        self.blackRadioButton.toggled.connect(Widget.backgroundChanged)
        self.whiteRadioButton.toggled.connect(Widget.backgroundChanged)
        self.autozoomButton.clicked.connect(Widget.autozoomClicked)
        self.gridCheckBox.stateChanged.connect(Widget.gridClicked)
        self.exportButton.clicked.connect(Widget.exportButtonClicked)
        self.radioButtonArea.toggled.connect(Widget.zoomModeChanged)
        self.layersWidget.tabBarClicked.connect(Widget.layerChanged)

        self.dataButton.setDefault(False)
        self.layersWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"sok-viewer", None))
        self.valuesLabel.setText(QCoreApplication.translate("Widget", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.zoomBox.setTitle("")
        self.radioButtonXY.setText(QCoreApplication.translate("Widget", u"X, Y", None))
        self.radioButtonX.setText(QCoreApplication.translate("Widget", u"X", None))
        self.radioButtonY.setText(QCoreApplication.translate("Widget", u"Y", None))
        self.radioButtonArea.setText(QCoreApplication.translate("Widget", u"\u041e\u0431\u043b\u0430\u0441\u0442\u044c", None))
        self.gridCheckBox.setText(QCoreApplication.translate("Widget", u"\u0421\u0435\u0442\u043a\u0430", None))
        self.backgroundLabel.setText(QCoreApplication.translate("Widget", u"\u0424\u043e\u043d", None))
        self.scaleLabel.setText(QCoreApplication.translate("Widget", u"\u0420\u0435\u0436\u0438\u043c", None))
        self.backgroundBox.setTitle("")
        self.blackRadioButton.setText(QCoreApplication.translate("Widget", u"\u0427\u0435\u0440\u043d\u044b\u0439", None))
        self.whiteRadioButton.setText(QCoreApplication.translate("Widget", u"\u0411\u0435\u043b\u044b\u0439", None))
        self.autozoomButton.setText(QCoreApplication.translate("Widget", u"\u0410\u0432\u0442\u043e", None))
        self.parametersLabel.setText(QCoreApplication.translate("Widget", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.controlBox.setTitle("")
        self.dataButton.setText(QCoreApplication.translate("Widget", u"\u0424\u0430\u0439\u043b", None))
        self.exportButton.setText(QCoreApplication.translate("Widget", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.fileStatusLabel.setText("")
        self.layersWidget.setTabText(self.layersWidget.indexOf(self.layer1), QCoreApplication.translate("Widget", u"1", None))
        self.layersWidget.setTabText(self.layersWidget.indexOf(self.layer2), QCoreApplication.translate("Widget", u"2", None))
        self.layersWidget.setTabText(self.layersWidget.indexOf(self.layer3), QCoreApplication.translate("Widget", u"3", None))
        self.layersWidget.setTabText(self.layersWidget.indexOf(self.layer4), QCoreApplication.translate("Widget", u"4", None))
        self.layersWidget.setTabText(self.layersWidget.indexOf(self.layer5), QCoreApplication.translate("Widget", u"5", None))
    # retranslateUi

