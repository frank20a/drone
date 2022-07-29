# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'monitor.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateTimeEdit,
    QGraphicsView, QHBoxLayout, QLCDNumber, QLabel,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1350, 750)
        MainWindow.setMinimumSize(QSize(1350, 750))
        MainWindow.setMaximumSize(QSize(1350, 750))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 211, 31))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.battery = QProgressBar(self.layoutWidget)
        self.battery.setObjectName(u"battery")
        self.battery.setValue(24)

        self.horizontalLayout_7.addWidget(self.battery)

        self.camera = QGraphicsView(self.centralwidget)
        self.camera.setObjectName(u"camera")
        self.camera.setGeometry(QRect(1050, 10, 288, 162))
        self.gps_status = QLabel(self.centralwidget)
        self.gps_status.setObjectName(u"gps_status")
        self.gps_status.setGeometry(QRect(950, 10, 91, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gps_status.sizePolicy().hasHeightForWidth())
        self.gps_status.setSizePolicy(sizePolicy)
        self.gps_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gps_status.setWordWrap(False)
        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(1090, 180, 212, 191))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(100, 0))
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.thrust = QSlider(self.layoutWidget_2)
        self.thrust.setObjectName(u"thrust")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.thrust.sizePolicy().hasHeightForWidth())
        self.thrust.setSizePolicy(sizePolicy2)
        self.thrust.setMaximum(500)
        self.thrust.setOrientation(Qt.Vertical)

        self.verticalLayout_4.addWidget(self.thrust)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMinimumSize(QSize(100, 0))
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_6)

        self.pitch = QSlider(self.layoutWidget_2)
        self.pitch.setObjectName(u"pitch")
        sizePolicy2.setHeightForWidth(self.pitch.sizePolicy().hasHeightForWidth())
        self.pitch.setSizePolicy(sizePolicy2)
        self.pitch.setMinimum(-250)
        self.pitch.setMaximum(250)
        self.pitch.setOrientation(Qt.Vertical)

        self.verticalLayout_5.addWidget(self.pitch)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setGeometry(QRect(10, 500, 311, 200))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.horizontalLayoutWidget_2 = QWidget(self.tab_1)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 30, 281, 111))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.calibrate_btn = QPushButton(self.horizontalLayoutWidget_2)
        self.calibrate_btn.setObjectName(u"calibrate_btn")
        sizePolicy3.setHeightForWidth(self.calibrate_btn.sizePolicy().hasHeightForWidth())
        self.calibrate_btn.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.calibrate_btn)

        self.arm_btn = QPushButton(self.horizontalLayoutWidget_2)
        self.arm_btn.setObjectName(u"arm_btn")
        sizePolicy3.setHeightForWidth(self.arm_btn.sizePolicy().hasHeightForWidth())
        self.arm_btn.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.arm_btn)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_2)

        self.buzzer_cmd_combo = QComboBox(self.horizontalLayoutWidget_2)
        self.buzzer_cmd_combo.addItem("")
        self.buzzer_cmd_combo.addItem("")
        self.buzzer_cmd_combo.addItem("")
        self.buzzer_cmd_combo.addItem("")
        self.buzzer_cmd_combo.addItem("")
        self.buzzer_cmd_combo.addItem("")
        self.buzzer_cmd_combo.setObjectName(u"buzzer_cmd_combo")

        self.verticalLayout_2.addWidget(self.buzzer_cmd_combo)

        self.buzzer_cmd_btn = QPushButton(self.horizontalLayoutWidget_2)
        self.buzzer_cmd_btn.setObjectName(u"buzzer_cmd_btn")
        sizePolicy3.setHeightForWidth(self.buzzer_cmd_btn.sizePolicy().hasHeightForWidth())
        self.buzzer_cmd_btn.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.buzzer_cmd_btn)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.tabs.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayoutWidget = QWidget(self.tab_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 50, 281, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.takeoff_btn = QPushButton(self.horizontalLayoutWidget)
        self.takeoff_btn.setObjectName(u"takeoff_btn")
        sizePolicy3.setHeightForWidth(self.takeoff_btn.sizePolicy().hasHeightForWidth())
        self.takeoff_btn.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.takeoff_btn)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy3.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.tabs.addTab(self.tab_2, "")
        self.layoutWidget_4 = QWidget(self.centralwidget)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(1060, 380, 271, 51))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.roll = QSlider(self.layoutWidget_4)
        self.roll.setObjectName(u"roll")
        self.roll.setMinimum(-250)
        self.roll.setMaximum(250)
        self.roll.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.roll)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.layoutWidget_4)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.yaw = QSlider(self.layoutWidget_4)
        self.yaw.setObjectName(u"yaw")
        self.yaw.setMinimum(-250)
        self.yaw.setMaximum(250)
        self.yaw.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.yaw)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.compass = QGraphicsView(self.centralwidget)
        self.compass.setObjectName(u"compass")
        self.compass.setGeometry(QRect(1230, 560, 110, 110))
        self.layoutWidget_3 = QWidget(self.centralwidget)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(1110, 670, 229, 28))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.gps_time = QDateTimeEdit(self.layoutWidget_3)
        self.gps_time.setObjectName(u"gps_time")
        self.gps_time.setReadOnly(False)
        self.gps_time.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.gps_time.setCalendarPopup(False)
        self.gps_time.setTimeSpec(Qt.UTC)

        self.horizontalLayout_6.addWidget(self.gps_time)

        self.azimuth = QGraphicsView(self.centralwidget)
        self.azimuth.setObjectName(u"azimuth")
        self.azimuth.setGeometry(QRect(1110, 560, 110, 110))
        self.layoutWidget_5 = QWidget(self.centralwidget)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(890, 640, 104, 61))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget_5)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.label_9)

        self.ping_height = QLCDNumber(self.layoutWidget_5)
        self.ping_height.setObjectName(u"ping_height")
        self.ping_height.setSmallDecimalPoint(False)
        self.ping_height.setMode(QLCDNumber.Dec)
        self.ping_height.setProperty("value", 12.340000000000000)

        self.verticalLayout_6.addWidget(self.ping_height)

        self.layoutWidget_6 = QWidget(self.centralwidget)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(1000, 640, 104, 61))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget_6)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.label_10)

        self.alt = QLCDNumber(self.layoutWidget_6)
        self.alt.setObjectName(u"alt")
        self.alt.setSmallDecimalPoint(False)
        self.alt.setDigitCount(5)
        self.alt.setMode(QLCDNumber.Dec)
        self.alt.setProperty("value", 12.340000000000000)

        self.verticalLayout_7.addWidget(self.alt)

        self.map = QWebEngineView(self.centralwidget)
        self.map.setObjectName(u"map")
        self.map.setGeometry(QRect(0, 0, 1350, 710))
        MainWindow.setCentralWidget(self.centralwidget)
        self.map.raise_()
        self.layoutWidget.raise_()
        self.camera.raise_()
        self.gps_status.raise_()
        self.layoutWidget_2.raise_()
        self.tabs.raise_()
        self.layoutWidget_4.raise_()
        self.compass.raise_()
        self.layoutWidget_3.raise_()
        self.azimuth.raise_()
        self.layoutWidget_5.raise_()
        self.layoutWidget_6.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1350, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(0)
        self.buzzer_cmd_combo.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Battery: ", None))
        self.gps_status.setText(QCoreApplication.translate("MainWindow", u"GPS Status", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Thrust", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Motors", None))
        self.calibrate_btn.setText(QCoreApplication.translate("MainWindow", u"Calibrate", None))
        self.arm_btn.setText(QCoreApplication.translate("MainWindow", u"Arm", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Buzzer", None))
        self.buzzer_cmd_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Single", None))
        self.buzzer_cmd_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Double", None))
        self.buzzer_cmd_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Long", None))
        self.buzzer_cmd_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"Error", None))
        self.buzzer_cmd_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"On", None))
        self.buzzer_cmd_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"Off", None))

        self.buzzer_cmd_btn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Low-Level", None))
        self.takeoff_btn.setText(QCoreApplication.translate("MainWindow", u"Take off", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Land", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Return\n"
"Home", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Flight", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"GPS Time", None))
        self.gps_time.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/mm/yyyy - hh:mm", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Ping Height(m)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Altitude (m)", None))
    # retranslateUi

