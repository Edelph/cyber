# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_client.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_client(object):
    def setupUi(self, add_client):
        add_client.setObjectName("add_client")
        add_client.resize(207, 201)
        self.label_title = QtWidgets.QLabel(add_client)
        self.label_title.setGeometry(QtCore.QRect(10, 10, 174, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.widget = QtWidgets.QWidget(add_client)
        self.widget.setGeometry(QtCore.QRect(10, 90, 181, 70))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_condition = QtWidgets.QCheckBox(self.widget)
        self.checkBox_condition.setObjectName("checkBox_condition")
        self.verticalLayout.addWidget(self.checkBox_condition)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_duree = QtWidgets.QRadioButton(self.widget)
        self.radioButton_duree.setObjectName("radioButton_duree")
        self.horizontalLayout.addWidget(self.radioButton_duree)
        self.radioButton_couts = QtWidgets.QRadioButton(self.widget)
        self.radioButton_couts.setObjectName("radioButton_couts")
        self.horizontalLayout.addWidget(self.radioButton_couts)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lineEdit_condition = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_condition.setObjectName("lineEdit_condition")
        self.verticalLayout.addWidget(self.lineEdit_condition)
        self.widget1 = QtWidgets.QWidget(add_client)
        self.widget1.setGeometry(QtCore.QRect(10, 170, 181, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_cancel = QtWidgets.QPushButton(self.widget1)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.btn_ajouter = QtWidgets.QPushButton(self.widget1)
        self.btn_ajouter.setObjectName("btn_ajouter")
        self.horizontalLayout_2.addWidget(self.btn_ajouter)
        self.widget2 = QtWidgets.QWidget(add_client)
        self.widget2.setGeometry(QtCore.QRect(10, 60, 181, 22))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_name = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout_3.addWidget(self.label_name)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout_3.addWidget(self.lineEdit_name)

        self.retranslateUi(add_client)
        QtCore.QMetaObject.connectSlotsByName(add_client)

    def retranslateUi(self, add_client):
        _translate = QtCore.QCoreApplication.translate
        add_client.setWindowTitle(_translate("add_client", "Form"))
        self.label_title.setText(_translate("add_client", "ajouter un utilisateur"))
        self.checkBox_condition.setText(_translate("add_client", "condition"))
        self.radioButton_duree.setText(_translate("add_client", "duree"))
        self.radioButton_couts.setText(_translate("add_client", "couts"))
        self.btn_cancel.setText(_translate("add_client", "cancel"))
        self.btn_ajouter.setText(_translate("add_client", "ajouter"))
        self.label_name.setText(_translate("add_client", "nom:"))




class AddClient(QtWidgets.QWidget, Ui_add_client):
    cancelWindows = QtCore.pyqtSignal()
    btn_ajouter_clicked = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self) 

        self.radioButton_couts.setEnabled(False)
        self.radioButton_duree.setEnabled(False)
        self.lineEdit_condition.setEnabled(False)
        self.lineEdit_condition.setEnabled(False)


        self.checkBox_condition.toggled.connect(self.checkBox_condition_checked)
        self.btn_cancel.clicked.connect(self.btn_cancel_handle)
        self.btn_ajouter.clicked.connect(self.btn_ajouter_handle)


    def checkBox_condition_checked(self,state):
        if state:
            self.radioButton_couts.setEnabled(True)
            self.radioButton_duree.setEnabled(True)
            self.radioButton_duree.setChecked(True)
            self.lineEdit_condition.setEnabled(True)

        else:
            self.radioButton_couts.setEnabled(False)
            self.radioButton_duree.setEnabled(False)

            self.lineEdit_condition.setEnabled(False)
    def btn_cancel_handle(self):
        self.cancelWindows.emit()

    def btn_ajouter_handle(self):
        duree = None
        cout = None
        name = self.lineEdit_name.text()


        if self.checkBox_condition.isChecked():
            if self.radioButton_couts.isChecked():
                cout = self.lineEdit_condition.text() 
            else:
                duree = self.lineEdit_condition.text()

        print(duree)
        print(cout)
        print(name)

        self.btn_ajouter_clicked.emit()


            

        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = AddClient()
    ui.cancelWindows.connect(ui.close)
    ui.show()
    sys.exit(app.exec_())
