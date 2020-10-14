# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainClients.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread,pyqtSignal
import time
from datetime import date
import sqlite3

class Ui_mainClients(object):
    def setupUi(self, mainClients):
        mainClients.setObjectName("mainClients")
        mainClients.resize(587, 457)
        mainClients.setStyleSheet("QLabel{\n"
"color:#fff\n"
"}\n"
"\n"
"\n"
"#comboBox_search{\n"
"background-color:#312f4c;\n"
"color:#fff\n"
"\n"
"}\n"
"QLineEdit{\n"
"background-color:#686868;\n"
"color:#fff;\n"
"border:none;\n"
"border-radius:3px\n"
"}\n"
"\n"
"#mainClients{\n"
"background-color:#494949;\n"
"\n"
"}\n"
"QPushButton{\n"
"border:1px solid black;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"background-color:#312f4c;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#686868\n"
"}")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(mainClients)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(mainClients)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tableWidget_listeClient = QtWidgets.QTableWidget(mainClients)
        self.tableWidget_listeClient.setStyleSheet("#tableWidget_listeClient{\n"
"background-color:#adadad\n"
"}")
        self.tableWidget_listeClient.setObjectName("tableWidget_listeClient")
        self.tableWidget_listeClient.setColumnCount(3)
        self.tableWidget_listeClient.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_listeClient.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_listeClient.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget_listeClient.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_8.addWidget(self.tableWidget_listeClient)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_titleAddClient = QtWidgets.QLabel(mainClients)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_titleAddClient.setFont(font)
        self.label_titleAddClient.setTextFormat(QtCore.Qt.AutoText)
        self.label_titleAddClient.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titleAddClient.setObjectName("label_titleAddClient")
        self.verticalLayout.addWidget(self.label_titleAddClient)
        self.lineEdit_newName = QtWidgets.QLineEdit(mainClients)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        self.lineEdit_newName.setFont(font)
        self.lineEdit_newName.setObjectName("lineEdit_newName")
        self.verticalLayout.addWidget(self.lineEdit_newName)
        self.btn_addClient = QtWidgets.QPushButton(mainClients)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setItalic(False)
        self.btn_addClient.setFont(font)
        self.btn_addClient.setObjectName("btn_addClient")
        self.verticalLayout.addWidget(self.btn_addClient)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(168, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_titleCurrentClient = QtWidgets.QLabel(mainClients)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_titleCurrentClient.setFont(font)
        self.label_titleCurrentClient.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titleCurrentClient.setObjectName("label_titleCurrentClient")
        self.verticalLayout_2.addWidget(self.label_titleCurrentClient)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_name = QtWidgets.QLabel(mainClients)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        self.lineEdit_name = QtWidgets.QLineEdit(mainClients)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout.addWidget(self.lineEdit_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_duree = QtWidgets.QLabel(mainClients)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_duree.setFont(font)
        self.label_duree.setObjectName("label_duree")
        self.horizontalLayout_2.addWidget(self.label_duree)
        self.lineEdit_duree = QtWidgets.QLineEdit(mainClients)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        self.lineEdit_duree.setFont(font)
        self.lineEdit_duree.setObjectName("lineEdit_duree")
        self.horizontalLayout_2.addWidget(self.lineEdit_duree)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_cout = QtWidgets.QLabel(mainClients)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_cout.setFont(font)
        self.label_cout.setObjectName("label_cout")
        self.horizontalLayout_3.addWidget(self.label_cout)
        self.lineEdit_cout = QtWidgets.QLineEdit(mainClients)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        self.lineEdit_cout.setFont(font)
        self.lineEdit_cout.setObjectName("lineEdit_cout")
        self.horizontalLayout_3.addWidget(self.lineEdit_cout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_pausePlay = QtWidgets.QPushButton(mainClients)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.btn_pausePlay.setFont(font)
        self.btn_pausePlay.setObjectName("btn_pausePlay")
        self.horizontalLayout_4.addWidget(self.btn_pausePlay)
        self.btn_stop = QtWidgets.QPushButton(mainClients)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.btn_stop.setFont(font)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout_4.addWidget(self.btn_stop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.horizontalLayout_8.setStretch(0, 4)
        self.horizontalLayout_8.setStretch(1, 2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_viewDB = QtWidgets.QPushButton(mainClients)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.btn_viewDB.setFont(font)
        self.btn_viewDB.setObjectName("btn_viewDB")
        self.horizontalLayout_6.addWidget(self.btn_viewDB)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_coutNow = QtWidgets.QLabel(mainClients)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_coutNow.setFont(font)
        self.label_coutNow.setObjectName("label_coutNow")
        self.horizontalLayout_5.addWidget(self.label_coutNow)
        self.lineEdit_coutNow = QtWidgets.QLineEdit(mainClients)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        self.lineEdit_coutNow.setFont(font)
        self.lineEdit_coutNow.setObjectName("lineEdit_coutNow")
        self.horizontalLayout_5.addWidget(self.lineEdit_coutNow)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_7.setStretch(0, 5)
        self.horizontalLayout_7.setStretch(1, 3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 10)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.retranslateUi(mainClients)
        QtCore.QMetaObject.connectSlotsByName(mainClients)

    def retranslateUi(self, mainClients):
        _translate = QtCore.QCoreApplication.translate
        mainClients.setWindowTitle(_translate("mainClients", "Form"))
        self.label.setText(_translate("mainClients", "les clients connectés"))
        item = self.tableWidget_listeClient.horizontalHeaderItem(0)
        item.setText(_translate("mainClients", "nom"))
        item = self.tableWidget_listeClient.horizontalHeaderItem(1)
        item.setText(_translate("mainClients", "duree"))
        item = self.tableWidget_listeClient.horizontalHeaderItem(2)
        item.setText(_translate("mainClients", "cout"))
        self.label_titleAddClient.setText(_translate("mainClients", "ajout un client(e)"))
        self.lineEdit_newName.setPlaceholderText(_translate("mainClients", " nouveau nom"))
        self.btn_addClient.setText(_translate("mainClients", "ajout"))
        self.label_titleCurrentClient.setText(_translate("mainClients", "client(e) sélectioné(e)"))
        self.label_name.setText(_translate("mainClients", "nom:"))
        self.label_duree.setText(_translate("mainClients", "duree:"))
        self.label_cout.setText(_translate("mainClients", "cout:"))
        self.btn_pausePlay.setText(_translate("mainClients", "pause"))
        self.btn_stop.setText(_translate("mainClients", "stop"))
        self.btn_viewDB.setText(_translate("mainClients", "voir tous les biens"))
        self.label_coutNow.setText(_translate("mainClients", "cout now:"))


class MainClients(QtWidgets.QWidget, Ui_mainClients):
    switch_window_viewDB = pyqtSignal()
    """docstring for MainClients"""
    row = -1
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.setTablewidget = []

        self.setupUi(self)

        self.btn_pausePlay.clicked.connect(self.btn_pausePlay_handle)
        self.tableWidget_listeClient.itemClicked.connect(self.clicOneItem)
        self.btn_addClient.clicked.connect(self.btn_addClient_handle)
        self.btn_viewDB.clicked.connect(self.btn_viewDB_handle)
        self.btn_stop.clicked.connect(self.btn_stop_handle)


    def btn_pausePlay_handle(self):
        if self.setTablewidget[MainClients.row].pauseIndice == 1:
            self.btn_pausePlay.setText("pause")
            self.setTablewidget[MainClients.row].play()
        else:
            self.btn_pausePlay.setText("play")
            self.setTablewidget[MainClients.row].pause()

        MainClients.row = -1




    def btn_addClient_handle(self):
        name = self.lineEdit_newName.text()
        self.setTablewidget.append(SetTablewidget(self.tableWidget_listeClient,name))
        self.lineEdit_newName.setText("")

    def clicOneItem(self,item):
        MainClients.row = self.tableWidget_listeClient.currentRow()
        self.tableWidget_listeClient.itemChanged.connect(self.printOneLineEdite)

        if self.setTablewidget[MainClients.row].pauseIndice == 0:
            self.btn_pausePlay.setText("pause")
        else:
            self.btn_pausePlay.setText("play")
    


    def btn_viewDB_handle(self):
        self.switch_window_viewDB.emit()

    def btn_stop_handle(self):

        tabRowCount = self.tableWidget_listeClient.rowCount()

        self.tableWidget_listeClient.setRowCount(tabRowCount)

        i=0
        j=0

        while i < tabRowCount :
            if i == MainClients.row :
                self.setTablewidget[i].setRow(tabRowCount-1)
            else:
                self.setTablewidget[i].setRow(j)
                j = j + 1
                
            i = i + 1

        self.tableWidget_listeClient.removeRow(0)
        del self.setTablewidget[MainClients.row]
        self.insertIntoDb(self.lineEdit_name.text(),self.lineEdit_duree.text(),self.lineEdit_cout.text())

        self.lineEdit_name.setText('')
        self.lineEdit_cout.setText('')
        self.lineEdit_duree.setText('')
        MainClients.row = -1

    def insertIntoDb(self,name,duree,cost):
        conn = sqlite3.connect('other/icons/cyber2.db')
        dd = date.today()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tableClient (name,duree,cost,dateNow) VALUES (?,?,?,?)",(name,duree,int(cost),dd))
        conn.commit()
        conn.close()
        
    def printOneLineEdite(self,item):
        if MainClients.row != -1 :
            self.lineEdit_name.setText(item.tableWidget().item(MainClients.row,0).text())
            self.lineEdit_cout.setText(item.tableWidget().item(MainClients.row,2).text())
            self.lineEdit_duree.setText(item.tableWidget().item(MainClients.row,1).text()) 

class SetTablewidget():

    def __init__(self,table,name):
        self.pauseIndice = 0
        self.table = table
        self.rowNow = self.table.rowCount()
        self.tread = MyTread()
        self.tread.change_value.connect(self.setlineedit)
        self.table.setRowCount(self.rowNow+1)
        self.tread.start()
        self.name=name

    def setRow(self,newRow):
        self.rowNow = newRow
        self.tread.change_value.connect(self.setlineedit)
        self.tread.start()

    def pause(self):
        self.tread.pause = True
        self.pauseIndice = 1

    def play(self):
        self.tread.pause = False
        self.tread.change_value.connect(self.setlineedit)
        self.tread.start()
        self.pauseIndice = 0

    def setlineedit(self,h,m,s,p):
        string = str(h)+"h "+str(m)+"m "+str(s)+"s "

        self.table.setItem(self.rowNow,0, QtWidgets.QTableWidgetItem(str(self.name)))
        self.table.setItem(self.rowNow,2, QtWidgets.QTableWidgetItem(str(p)))
        self.table.setItem(self.rowNow,1, QtWidgets.QTableWidgetItem(str(string)))



class MyTread(QThread):
    change_value = pyqtSignal(int ,int ,int, int)

    def __init__(self):
        QThread.__init__(self)
        self.prix = 500
        self.pause = False
        self.state = 0
        self.hour = 0
        self.minute = 0
        self.second = 0

    def run(self):
        if self.pause == True:
            self.change_value.emit(self.hour, self.minute, self.second,self.prix)
        else:
            self.startChrono(self.hour, self.minute, self.second)


    def startChrono(self, hour, minute, second):  
        while self.state <= self.prix:
            self.change_value.emit(self.hour, self.minute, self.second,self.prix)
            if self.pause == True:
                break
            else:
                time.sleep(1)
                self.second += 1
                if self.second == 60:
                    self.minute += 1
                    self.state += 30
                    self.second = 0
                    if self.minute == 60:
                        self.minute=0
                        self.hour += 1

                if self.state  > (self.prix-10):
                    self.prix += 100

        

        
