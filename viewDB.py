# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewDB.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from math import ceil

class Ui_Uaffichage(object):
    def setupUi(self, Uaffichage):
        Uaffichage.setObjectName("Uaffichage")
        Uaffichage.resize(445, 473)
        Uaffichage.setStyleSheet("#Uaffichage{\n"
"background-color:#494949;\n"
"}\n"
"\n"
"QLabel{\n"
"color:#000\n"
"}\n"
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Uaffichage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_title = QtWidgets.QLabel(Uaffichage)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        self.comboBox_search = QtWidgets.QComboBox(Uaffichage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_search.setFont(font)
        self.comboBox_search.setObjectName("comboBox_search")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_search)
        self.lineEdit_search = QtWidgets.QLineEdit(Uaffichage)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        self.lineEdit_search.setFont(font)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout.addWidget(self.lineEdit_search)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget_data = QtWidgets.QTableWidget(Uaffichage)
        self.tableWidget_data.setStyleSheet("#tableWidget_data{\n"
"background-color:#adadad\n"
"\n"
"}")
        self.tableWidget_data.setRowCount(0)
        self.tableWidget_data.setColumnCount(4)
        self.tableWidget_data.setObjectName("tableWidget_data")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_data.setHorizontalHeaderItem(3, item)
        self.tableWidget_data.horizontalHeader().setVisible(True)
        self.tableWidget_data.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_data.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_data.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget_data)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_previous = QtWidgets.QPushButton(Uaffichage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.btn_previous.setFont(font)
        self.btn_previous.setObjectName("btn_previous")
        self.horizontalLayout_2.addWidget(self.btn_previous)
        self.label_page = QtWidgets.QLabel(Uaffichage)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.label_page.setFont(font)
        self.label_page.setAlignment(QtCore.Qt.AlignCenter)
        self.label_page.setObjectName("label_page")
        self.horizontalLayout_2.addWidget(self.label_page)
        self.btn_next = QtWidgets.QPushButton(Uaffichage)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.btn_next.setFont(font)
        self.btn_next.setObjectName("btn_next")
        self.horizontalLayout_2.addWidget(self.btn_next)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_total = QtWidgets.QLabel(Uaffichage)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_total.setFont(font)
        self.label_total.setObjectName("label_total")
        self.horizontalLayout_3.addWidget(self.label_total)
        self.lineEdit_total = QtWidgets.QLineEdit(Uaffichage)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        self.lineEdit_total.setFont(font)
        self.lineEdit_total.setObjectName("lineEdit_total")
        self.horizontalLayout_3.addWidget(self.lineEdit_total)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.setStretch(0, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Uaffichage)
        QtCore.QMetaObject.connectSlotsByName(Uaffichage)

    def retranslateUi(self, Uaffichage):
        _translate = QtCore.QCoreApplication.translate
        Uaffichage.setWindowTitle(_translate("Uaffichage", "Form"))
        self.label_title.setText(_translate("Uaffichage", "tous les biens"))
        self.comboBox_search.setItemText(0, _translate("Uaffichage", "nom"))
        self.comboBox_search.setItemText(1, _translate("Uaffichage", "dates"))
        self.lineEdit_search.setPlaceholderText(_translate("Uaffichage", "searcch"))
        item = self.tableWidget_data.horizontalHeaderItem(0)
        item.setText(_translate("Uaffichage", "nom"))
        item = self.tableWidget_data.horizontalHeaderItem(1)
        item.setText(_translate("Uaffichage", "dure"))
        item = self.tableWidget_data.horizontalHeaderItem(2)
        item.setText(_translate("Uaffichage", "prix"))
        item = self.tableWidget_data.horizontalHeaderItem(3)
        item.setText(_translate("Uaffichage", "dates"))
        self.btn_previous.setText(_translate("Uaffichage", "previous"))
        self.label_page.setText(_translate("Uaffichage", "page"))
        self.btn_next.setText(_translate("Uaffichage", "next"))
        self.label_total.setText(_translate("Uaffichage", "total:"))



class Affichage(QtWidgets.QTabWidget, Ui_Uaffichage):
    currentPage = 1
    onePage = 20
    number_page = 1
    

    def __init__(self):
        QtWidgets.QTabWidget.__init__(self)
        self.setupUi(self)
        self.load(Affichage.currentPage)
        Affichage.number_page = ceil(self.countElementDb()/Affichage.onePage)
        self.lineEdit_search.textChanged.connect(self.lineEdit_search_textChanged)
        self.printPage()

        #definir tout les btn

        self.btn_next.clicked.connect(self.next_handle)
        self.btn_previous.clicked.connect(self.previous_handle)
    # on click sur btn next

    def printPage(self):
        if Affichage.number_page == 1 :
            page = " page"
        else:
            page = " pages"
        self.label_page.setText(str(Affichage.currentPage)+ "/" + str(Affichage.number_page)+ str(page))

    def next_handle(self):
        if Affichage.number_page > Affichage.currentPage:
            Affichage.currentPage += 1
            self.printPage()
            if self.lineEdit_search.text() == "":
                self.load(Affichage.currentPage)
            else:
                self.load(Affichage.currentPage,self.return_search(),self.lineEdit_search.text())

    # on click sur btn previous
    def previous_handle(self):
        if Affichage.currentPage > 1 :
            Affichage.currentPage -= 1
            self.printPage()
            if self.lineEdit_search.text() == "":
                self.load(Affichage.currentPage)
            else:
                self.load(Affichage.currentPage,self.return_search(),self.lineEdit_search.text())

    def return_search(self):
        indice = self.comboBox_search.currentText()
        if indice == "nom":
            search = "_name"
        else :
            search = "_date"
        return search

    def lineEdit_search_textChanged(self):
        Affichage.currentPage = 1
        lineEdit_search_text = self.lineEdit_search.text()
        indice = self.comboBox_search.currentText()
        search = self.return_search()
        if  search== None:
            return None

        Affichage.number_page = ceil(self.countElementDb(search,lineEdit_search_text)/Affichage.onePage)
        self.load(Affichage.currentPage,search,lineEdit_search_text)
        self.printPage()
            
    #conter tout les element dans le db 
    """
    *@search : colonne du table dans le db
    *@q      : les valeur taper par l'utilisateur
    *@return : int valeur du comteur
    """
    def countElementDb (self, search =  None , q = None):
        conn=sqlite3.connect('other/icons/cyber.db')
        sql = "SELECT COUNT (*) FROM client "

        if not(search == None):
            where = "%" + q +"%"
            sql = sql +"WHERE %s LIKE '%s'" % (search, where) 
        cursor = conn.cursor() 
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return int (result[0])


    def getDb(self, Cpage, search =  None , q = None):
        self.tableWidget_data.setRowCount(0)
        conn=sqlite3.connect('other/icons/cyber.db')
        cursor = conn.cursor()
        offset = Affichage.onePage * (Cpage-1)
        sql = "SELECT * FROM client "

        if not(search == None):
            where = "%" + q +"%"
            sql = sql +"WHERE %s LIKE '%s'" % (search, where) 
        
        sql = sql + " LIMIT '%d' OFFSET '%d'" % ( Affichage.onePage,offset)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()

        return result

    def load(self,Cpage, search =  None , q = None):
        self.tableWidget_data.setRowCount(0)
        result = self.getDb(Cpage,search, q)
        for rownumber , rowdata in enumerate(result):
            self.tableWidget_data.insertRow(rownumber)
            self.tableWidget_data.setItem(rownumber,0, QtWidgets.QTableWidgetItem(str(rowdata[1])))   
            self.tableWidget_data.setItem(rownumber,1, QtWidgets.QTableWidgetItem(str(rowdata[2])))       
            self.tableWidget_data.setItem(rownumber,2, QtWidgets.QTableWidgetItem(str(rowdata[3])))    
            rowdata = rowdata[2] * 20  
            self.tableWidget_data.setItem(rownumber,3, QtWidgets.QTableWidgetItem(str(rowdata)+ " Ar"))       

        