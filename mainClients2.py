# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainClients.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainClients(object):
    def setupUi(self, mainClients):
        mainClients.setObjectName("mainClients")
        mainClients.resize(645, 418)
        self.tableWidget_listeClient = QtWidgets.QTableWidget(mainClients)
        self.tableWidget_listeClient.setGeometry(QtCore.QRect(10, 70, 621, 301))
        self.tableWidget_listeClient.setObjectName("tableWidget_listeClient")
        self.tableWidget_listeClient.setColumnCount(3)
        self.tableWidget_listeClient.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_listeClient.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_listeClient.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_listeClient.setHorizontalHeaderItem(2, item)
        self.label_name = QtWidgets.QLabel(mainClients)
        self.label_name.setGeometry(QtCore.QRect(10, 40, 31, 16))
        self.label_name.setObjectName("label_name")
        self.lineEdit_name = QtWidgets.QLineEdit(mainClients)
        self.lineEdit_name.setGeometry(QtCore.QRect(40, 40, 101, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_duree = QtWidgets.QLabel(mainClients)
        self.label_duree.setGeometry(QtCore.QRect(160, 40, 31, 16))
        self.label_duree.setObjectName("label_duree")
        self.lineEdit_duree = QtWidgets.QLineEdit(mainClients)
        self.lineEdit_duree.setGeometry(QtCore.QRect(200, 40, 71, 20))
        self.lineEdit_duree.setObjectName("lineEdit_duree")
        self.lineEdit_cout = QtWidgets.QLineEdit(mainClients)
        self.lineEdit_cout.setGeometry(QtCore.QRect(310, 40, 71, 20))
        self.lineEdit_cout.setObjectName("lineEdit_cout")
        self.label_cout = QtWidgets.QLabel(mainClients)
        self.label_cout.setGeometry(QtCore.QRect(280, 40, 41, 16))
        self.label_cout.setObjectName("label_cout")
        self.btn_pausePlay = QtWidgets.QPushButton(mainClients)
        self.btn_pausePlay.setGeometry(QtCore.QRect(410, 40, 51, 23))
        self.btn_pausePlay.setObjectName("btn_pausePlay")
        self.btn_stop = QtWidgets.QPushButton(mainClients)
        self.btn_stop.setGeometry(QtCore.QRect(480, 40, 51, 23))
        self.btn_stop.setObjectName("btn_stop")
        self.label_coutNow = QtWidgets.QLabel(mainClients)
        self.label_coutNow.setGeometry(QtCore.QRect(460, 380, 61, 20))
        self.label_coutNow.setObjectName("label_coutNow")
        self.lineEdit_coutNow = QtWidgets.QLineEdit(mainClients)
        self.lineEdit_coutNow.setGeometry(QtCore.QRect(520, 380, 113, 20))
        self.lineEdit_coutNow.setObjectName("lineEdit_coutNow")
        self.lineEdit_search = QtWidgets.QLineEdit(mainClients)
        self.lineEdit_search.setGeometry(QtCore.QRect(10, 380, 131, 20))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.btn_addClient = QtWidgets.QPushButton(mainClients)
        self.btn_addClient.setGeometry(QtCore.QRect(560, 40, 71, 23))
        self.btn_addClient.setObjectName("btn_addClient")
        self.btn_viewDB = QtWidgets.QPushButton(mainClients)
        self.btn_viewDB.setGeometry(QtCore.QRect(250, 380, 151, 21))
        self.btn_viewDB.setObjectName("btn_viewDB")
        self.lineEdit_newName = QtWidgets.QLineEdit(mainClients)
        self.lineEdit_newName.setGeometry(QtCore.QRect(510, 10, 121, 20))
        self.lineEdit_newName.setObjectName("lineEdit_newName")

        self.retranslateUi(mainClients)
        QtCore.QMetaObject.connectSlotsByName(mainClients)

    def retranslateUi(self, mainClients):
        _translate = QtCore.QCoreApplication.translate
        mainClients.setWindowTitle(_translate("mainClients", "Form"))
        item = self.tableWidget_listeClient.horizontalHeaderItem(0)
        item.setText(_translate("mainClients", "nom"))
        item = self.tableWidget_listeClient.horizontalHeaderItem(1)
        item.setText(_translate("mainClients", "duree"))
        item = self.tableWidget_listeClient.horizontalHeaderItem(2)
        item.setText(_translate("mainClients", "cout"))
        self.label_name.setText(_translate("mainClients", "nom:"))
        self.label_duree.setText(_translate("mainClients", "duree:"))
        self.label_cout.setText(_translate("mainClients", "cout:"))
        self.btn_pausePlay.setText(_translate("mainClients", "pause"))
        self.btn_stop.setText(_translate("mainClients", "stop"))
        self.label_coutNow.setText(_translate("mainClients", "cout now:"))
        self.lineEdit_search.setPlaceholderText(_translate("mainClients", "search"))
        self.btn_addClient.setText(_translate("mainClients", "ajout"))
        self.btn_viewDB.setText(_translate("mainClients", "voir tous les biens"))
        self.lineEdit_newName.setPlaceholderText(_translate("mainClients", " nouveau nom"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainClients = QtWidgets.QWidget()
    ui = Ui_mainClients()
    ui.setupUi(mainClients)
    mainClients.show()
    sys.exit(app.exec_())
