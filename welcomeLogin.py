# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomeLogin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import other.icons.diverseIcons     


class Ui_welcomeLogin(object):
    def setupUi(self, welcomeLogin):
        welcomeLogin.setObjectName("welcomeLogin")
        welcomeLogin.resize(562, 342)
        self.frame_groupLogin = QtWidgets.QFrame(welcomeLogin)
        self.frame_groupLogin.setGeometry(QtCore.QRect(200, 10, 351, 321))
        self.frame_groupLogin.setStyleSheet("#frame_groupLogin{\n"
"border-image:url(:/photos/Background.jpg)\n"
"}\n"
"QLineEdit{\n"
"background-color:transparent;\n"
"border:none;\n"
"border-bottom:2px solid black;\n"
"color:#8c01a4;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:#3f5cdd;\n"
"border-radius:15px;\n"
"}\n"
"QLabel{\n"
"color:#fc003b;\n"
"}\n"
"#label_title{\n"
"color:#2828fe;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#8c01a4;\n"
"}")
        self.frame_groupLogin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_groupLogin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_groupLogin.setObjectName("frame_groupLogin")
        self.label_title = QtWidgets.QLabel(self.frame_groupLogin)
        self.label_title.setGeometry(QtCore.QRect(110, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.lineEdit_userName = QtWidgets.QLineEdit(self.frame_groupLogin)
        self.lineEdit_userName.setGeometry(QtCore.QRect(20, 110, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_userName.setFont(font)
        self.lineEdit_userName.setObjectName("lineEdit_userName")
        self.lineEdit_pswd = QtWidgets.QLineEdit(self.frame_groupLogin)
        self.lineEdit_pswd.setGeometry(QtCore.QRect(20, 200, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pswd.setFont(font)
        self.lineEdit_pswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pswd.setObjectName("lineEdit_pswd")
        self.btn_submit = QtWidgets.QPushButton(self.frame_groupLogin)
        self.btn_submit.setGeometry(QtCore.QRect(120, 272, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_submit.setFont(font)
        self.btn_submit.setObjectName("btn_submit")
        self.label_userName = QtWidgets.QLabel(self.frame_groupLogin)
        self.label_userName.setGeometry(QtCore.QRect(20, 70, 101, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.label_userName.setFont(font)
        self.label_userName.setObjectName("label_userName")
        self.label_pswd = QtWidgets.QLabel(self.frame_groupLogin)
        self.label_pswd.setGeometry(QtCore.QRect(20, 160, 101, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.label_pswd.setFont(font)
        self.label_pswd.setObjectName("label_pswd")
        self.frame_textBienvenue = QtWidgets.QFrame(welcomeLogin)
        self.frame_textBienvenue.setGeometry(QtCore.QRect(10, 10, 191, 321))
        self.frame_textBienvenue.setStyleSheet("#frame_textBienvenue{\n"
"border-image:url(:/photos/textBienvenue.jpg)\n"
"}")
        self.frame_textBienvenue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_textBienvenue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_textBienvenue.setObjectName("frame_textBienvenue")

        self.retranslateUi(welcomeLogin)
        QtCore.QMetaObject.connectSlotsByName(welcomeLogin)
       

    

    

    def retranslateUi(self, welcomeLogin):
        _translate = QtCore.QCoreApplication.translate
        welcomeLogin.setWindowTitle(_translate("welcomeLogin", "Form"))
        self.label_title.setText(_translate("welcomeLogin", "LOGIN"))
        self.btn_submit.setText(_translate("welcomeLogin", "submit"))
        self.label_userName.setText(_translate("welcomeLogin", "User Name:"))
        self.label_pswd.setText(_translate("welcomeLogin", "password:"))


class WelcomeLogin(QtWidgets.QWidget,Ui_welcomeLogin):
    """docstring for WelcomLogin"""
    switch_window_mainClient = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.setupUi(self)

        self.btn_submit.clicked.connect(self.btn_submit_handler)

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def btn_submit_handler(self):
        val = self.bool_check_username()

        if (val):
            self.pop_message(text="Welcome ")
            self.switch_window_mainClient.emit()

        else:
            self.pop_message("username or password invalid")

    def bool_check_username(self):
        if len(self.lineEdit_pswd.text()) <= 1 or len(self.lineEdit_userName.text()) <= 1:
            self.pop_message(text='Enter Valid Username and Password !')
        else:
            username = self.lineEdit_userName.text()
            password = self.lineEdit_pswd.text()
            conn = sqlite3.connect('other/icons/cyber.db')
            cursor = conn.cursor()
            cursor.execute("SELECT username,password FROM login")
            val = cursor.fetchall()
            if len(val) >= 1:
                for x in val:
                    if username in x[0] and password in x[1]:
                        return True
                    else:
                        pass
            else:
                self.pop_message(text="No users Found ")
                return False