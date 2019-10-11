# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p2_login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(768, 512)
        login.setMinimumSize(QtCore.QSize(768, 512))
        login.setMaximumSize(QtCore.QSize(768, 512))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        login.setFont(font)
        self.logi = QtWidgets.QFrame(login)
        self.logi.setGeometry(QtCore.QRect(30, 20, 701, 461))
        self.logi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logi.setObjectName("logi")
        self.pushButton_login = QtWidgets.QPushButton(self.logi)
        self.pushButton_login.setGeometry(QtCore.QRect(450, 380, 121, 41))
        self.pushButton_login.setObjectName("pushButton_login")
        self.lineEdit_account = QtWidgets.QLineEdit(self.logi)
        self.lineEdit_account.setGeometry(QtCore.QRect(260, 110, 221, 41))
        self.lineEdit_account.setMaxLength(6)
        self.lineEdit_account.setReadOnly(True)
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.lineEdit_password = QtWidgets.QLineEdit(self.logi)
        self.lineEdit_password.setGeometry(QtCore.QRect(260, 210, 221, 41))
        self.lineEdit_password.setMaxLength(8)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_register = QtWidgets.QPushButton(self.logi)
        self.pushButton_register.setGeometry(QtCore.QRect(100, 380, 121, 41))
        self.pushButton_register.setObjectName("pushButton_register")
        self.label = QtWidgets.QLabel(self.logi)
        self.label.setGeometry(QtCore.QRect(160, 100, 121, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.logi)
        self.label_2.setGeometry(QtCore.QRect(150, 200, 121, 51))
        self.label_2.setObjectName("label_2")
        self.pushButton_forgot = QtWidgets.QPushButton(self.logi)
        self.pushButton_forgot.setGeometry(QtCore.QRect(490, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_forgot.setFont(font)
        self.pushButton_forgot.setObjectName("pushButton_forgot")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)
        login.setTabOrder(self.lineEdit_account, self.lineEdit_password)
        login.setTabOrder(self.lineEdit_password, self.pushButton_login)
        login.setTabOrder(self.pushButton_login, self.pushButton_register)
        login.setTabOrder(self.pushButton_register, self.pushButton_forgot)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Welcome to use ESTRA CFD system V2.1"))
        self.pushButton_login.setText(_translate("login", "login"))
        self.lineEdit_password.setPlaceholderText(_translate("login", "Support for 8-bit"))
        self.pushButton_register.setText(_translate("login", "register"))
        self.label.setText(_translate("login", "Account"))
        self.label_2.setText(_translate("login", "Password"))
        self.pushButton_forgot.setText(_translate("login", "forgot"))
