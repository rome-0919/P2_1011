# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p2_function.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_function(object):
    def setupUi(self, function):
        function.setObjectName("function")
        function.resize(768, 512)
        function.setMinimumSize(QtCore.QSize(768, 512))
        function.setMaximumSize(QtCore.QSize(768, 512))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        function.setFont(font)
        self.func = QtWidgets.QFrame(function)
        self.func.setGeometry(QtCore.QRect(30, 20, 701, 461))
        self.func.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.func.setFrameShadow(QtWidgets.QFrame.Raised)
        self.func.setObjectName("func")
        self.pushButton_next = QtWidgets.QPushButton(self.func)
        self.pushButton_next.setGeometry(QtCore.QRect(520, 420, 121, 41))
        self.pushButton_next.setCheckable(False)
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_back = QtWidgets.QPushButton(self.func)
        self.pushButton_back.setGeometry(QtCore.QRect(70, 420, 121, 41))
        self.pushButton_back.setCheckable(False)
        self.pushButton_back.setObjectName("pushButton_back")
        self.scrollArea = QtWidgets.QScrollArea(self.func)
        self.scrollArea.setGeometry(QtCore.QRect(460, 60, 181, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scrollArea.setFont(font)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 179, 279))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_sphere = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_sphere.setCheckable(True)
        self.checkBox_sphere.setChecked(True)
        self.checkBox_sphere.setObjectName("checkBox_sphere")
        self.verticalLayout.addWidget(self.checkBox_sphere)
        self.checkBox_evap = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_evap.setChecked(True)
        self.checkBox_evap.setObjectName("checkBox_evap")
        self.verticalLayout.addWidget(self.checkBox_evap)
        self.checkBox_heater = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_heater.setChecked(False)
        self.checkBox_heater.setObjectName("checkBox_heater")
        self.verticalLayout.addWidget(self.checkBox_heater)
        self.checkBox_distributor = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_distributor.setChecked(True)
        self.checkBox_distributor.setObjectName("checkBox_distributor")
        self.verticalLayout.addWidget(self.checkBox_distributor)
        self.checkBox_tempdoor2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_tempdoor2.setEnabled(False)
        self.checkBox_tempdoor2.setChecked(False)
        self.checkBox_tempdoor2.setObjectName("checkBox_tempdoor2")
        self.verticalLayout.addWidget(self.checkBox_tempdoor2)
        self.checkBox_tempdoor1 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_tempdoor1.setEnabled(False)
        self.checkBox_tempdoor1.setChecked(False)
        self.checkBox_tempdoor1.setObjectName("checkBox_tempdoor1")
        self.verticalLayout.addWidget(self.checkBox_tempdoor1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_CG = QtWidgets.QPushButton(self.func)
        self.pushButton_CG.setGeometry(QtCore.QRect(70, 60, 201, 121))
        self.pushButton_CG.setMouseTracking(True)
        self.pushButton_CG.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_CG.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_CG.setAcceptDrops(False)
        self.pushButton_CG.setAutoFillBackground(False)
        self.pushButton_CG.setCheckable(True)
        self.pushButton_CG.setChecked(True)
        self.pushButton_CG.setAutoRepeat(False)
        self.pushButton_CG.setAutoExclusive(False)
        self.pushButton_CG.setAutoDefault(True)
        self.pushButton_CG.setDefault(False)
        self.pushButton_CG.setFlat(False)
        self.pushButton_CG.setObjectName("pushButton_CG")
        self.label_3 = QtWidgets.QLabel(self.func)
        self.label_3.setGeometry(QtCore.QRect(450, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.func)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(130, 270, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.func)
        self.label_2.setGeometry(QtCore.QRect(130, 120, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_XX = QtWidgets.QPushButton(self.func)
        self.pushButton_XX.setEnabled(False)
        self.pushButton_XX.setGeometry(QtCore.QRect(70, 200, 201, 121))
        self.pushButton_XX.setCheckable(True)
        self.pushButton_XX.setObjectName("pushButton_XX")
        self.toolButton_cool_hot = QtWidgets.QToolButton(self.func)
        self.toolButton_cool_hot.setGeometry(QtCore.QRect(220, 150, 51, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cool2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("hot2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_cool_hot.setIcon(icon)
        self.toolButton_cool_hot.setIconSize(QtCore.QSize(55, 33))
        self.toolButton_cool_hot.setCheckable(True)
        self.toolButton_cool_hot.setObjectName("toolButton_cool_hot")
        self.label_4 = QtWidgets.QLabel(self.func)
        self.label_4.setGeometry(QtCore.QRect(70, 350, 571, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.func)
        self.label_5.setGeometry(QtCore.QRect(60, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_next.raise_()
        self.pushButton_back.raise_()
        self.scrollArea.raise_()
        self.pushButton_CG.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.pushButton_XX.raise_()
        self.label.raise_()
        self.toolButton_cool_hot.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        self.retranslateUi(function)
        self.toolButton_cool_hot.clicked['bool'].connect(self.checkBox_heater.setChecked)
        self.checkBox_heater.clicked['bool'].connect(self.toolButton_cool_hot.setChecked)
        self.pushButton_CG.clicked.connect(self.toolButton_cool_hot.click)
        self.pushButton_CG.clicked['bool'].connect(self.checkBox_evap.setChecked)
        self.pushButton_CG.clicked['bool'].connect(self.checkBox_sphere.setChecked)
        self.pushButton_CG.clicked['bool'].connect(self.checkBox_distributor.setChecked)
        self.pushButton_XX.clicked['bool'].connect(self.checkBox_heater.setChecked)
        self.pushButton_XX.clicked['bool'].connect(self.checkBox_tempdoor1.setChecked)
        QtCore.QMetaObject.connectSlotsByName(function)
        function.setTabOrder(self.pushButton_XX, self.toolButton_cool_hot)
        function.setTabOrder(self.toolButton_cool_hot, self.checkBox_sphere)
        function.setTabOrder(self.checkBox_sphere, self.checkBox_evap)
        function.setTabOrder(self.checkBox_evap, self.checkBox_heater)
        function.setTabOrder(self.checkBox_heater, self.checkBox_distributor)
        function.setTabOrder(self.checkBox_distributor, self.checkBox_tempdoor2)
        function.setTabOrder(self.checkBox_tempdoor2, self.checkBox_tempdoor1)
        function.setTabOrder(self.checkBox_tempdoor1, self.pushButton_back)
        function.setTabOrder(self.pushButton_back, self.pushButton_next)
        function.setTabOrder(self.pushButton_next, self.scrollArea)

    def retranslateUi(self, function):
        _translate = QtCore.QCoreApplication.translate
        function.setWindowTitle(_translate("function", "function"))
        self.pushButton_next.setText(_translate("function", "next"))
        self.pushButton_back.setText(_translate("function", "back"))
        self.checkBox_sphere.setText(_translate("function", "sphere"))
        self.checkBox_evap.setText(_translate("function", "evap"))
        self.checkBox_heater.setText(_translate("function", "heater"))
        self.checkBox_distributor.setText(_translate("function", "distributor"))
        self.checkBox_tempdoor2.setText(_translate("function", "tempdoor2"))
        self.checkBox_tempdoor1.setText(_translate("function", "tempdoor1"))
        self.pushButton_CG.setText(_translate("function", "Regular\n"
""))
        self.label_3.setText(_translate("function", "check:"))
        self.label.setText(_translate("function", "（unavailable）"))
        self.label_2.setText(_translate("function", "（distribute &\n"
"pressure drop）"))
        self.pushButton_XX.setText(_translate("function", "Linearity\n"
""))
        self.toolButton_cool_hot.setText(_translate("function", "冷热切换"))
        self.label_4.setText(_translate("function", "Cautions: 1.Regular mode doesn\'t enable heater by default. If needed, please press \"cold/hot\" button.\n"
"                 2.Linearity function is not available at the moment."))
        self.label_5.setText(_translate("function", "quickly"))
