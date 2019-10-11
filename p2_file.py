# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p2_file.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_file(object):
    def setupUi(self, file):
        file.setObjectName("file")
        file.resize(768, 512)
        file.setMinimumSize(QtCore.QSize(768, 512))
        file.setMaximumSize(QtCore.QSize(768, 512))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        file.setFont(font)
        self.file_2 = QtWidgets.QFrame(file)
        self.file_2.setGeometry(QtCore.QRect(20, 20, 731, 461))
        self.file_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.file_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.file_2.setObjectName("file_2")
        self.toolButton_open = QtWidgets.QToolButton(self.file_2)
        self.toolButton_open.setGeometry(QtCore.QRect(600, 210, 51, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_open.setIcon(icon)
        self.toolButton_open.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_open.setObjectName("toolButton_open")
        self.lineEdit_version = QtWidgets.QLineEdit(self.file_2)
        self.lineEdit_version.setGeometry(QtCore.QRect(500, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_version.setFont(font)
        self.lineEdit_version.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEdit_version.setMaxLength(6)
        self.lineEdit_version.setClearButtonEnabled(True)
        self.lineEdit_version.setObjectName("lineEdit_version")
        self.pushButton_next = QtWidgets.QPushButton(self.file_2)
        self.pushButton_next.setGeometry(QtCore.QRect(510, 420, 121, 41))
        self.pushButton_next.setObjectName("pushButton_next")
        self.label_3 = QtWidgets.QLabel(self.file_2)
        self.label_3.setGeometry(QtCore.QRect(110, 180, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.file_2)
        self.label_2.setGeometry(QtCore.QRect(410, 110, 81, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_file = QtWidgets.QLineEdit(self.file_2)
        self.lineEdit_file.setGeometry(QtCore.QRect(110, 210, 481, 41))
        self.lineEdit_file.setReadOnly(True)
        self.lineEdit_file.setClearButtonEnabled(True)
        self.lineEdit_file.setObjectName("lineEdit_file")
        self.lineEdit_project = QtWidgets.QLineEdit(self.file_2)
        self.lineEdit_project.setGeometry(QtCore.QRect(200, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_project.setFont(font)
        self.lineEdit_project.setText("")
        self.lineEdit_project.setMaxLength(10)
        self.lineEdit_project.setClearButtonEnabled(True)
        self.lineEdit_project.setObjectName("lineEdit_project")
        self.label = QtWidgets.QLabel(self.file_2)
        self.label.setGeometry(QtCore.QRect(110, 110, 81, 31))
        self.label.setObjectName("label")
        self.label_note = QtWidgets.QLabel(self.file_2)
        self.label_note.setGeometry(QtCore.QRect(110, 280, 541, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_note.setFont(font)
        self.label_note.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.label_note.setLineWidth(3)
        self.label_note.setTextFormat(QtCore.Qt.PlainText)
        self.label_note.setObjectName("label_note")

        self.retranslateUi(file)
        QtCore.QMetaObject.connectSlotsByName(file)
        file.setTabOrder(self.lineEdit_project, self.lineEdit_version)
        file.setTabOrder(self.lineEdit_version, self.lineEdit_file)
        file.setTabOrder(self.lineEdit_file, self.toolButton_open)
        file.setTabOrder(self.toolButton_open, self.pushButton_next)

    def retranslateUi(self, file):
        _translate = QtCore.QCoreApplication.translate
        file.setWindowTitle(_translate("file", "project & version"))
        self.toolButton_open.setText(_translate("file", "..."))
        self.lineEdit_version.setPlaceholderText(_translate("file", "V1.0.1"))
        self.pushButton_next.setText(_translate("file", "next"))
        self.label_3.setText(_translate("file", "Choose CAD file："))
        self.label_2.setText(_translate("file", "Version"))
        self.label.setText(_translate("file", "Project"))
        self.label_note.setText(_translate("file", "Note: filename and filepath can\'t contain space ! ! !\n"
"          only supports numbers, letters, underscores\n"
"          the first character of version must be V, supporting numbers and decimal points"))
