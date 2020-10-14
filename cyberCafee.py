import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5 import QtWidgets
from welcomeLogin import *
from mainClients import *
from viewDB import *


class Controller:

    def __init__(self):
        pass

    def show_welcom_login_page(self):
        self.login = WelcomeLogin()
        self.login.switch_window_mainClient.connect(self.show_mainClient_page)
        self.login.show()

    def show_db(self):
    	self.affichage = Affichage()
    	self.affichage.show()


    def show_mainClient_page(self):
        self.mainClients = MainClients()
        self.mainClients.switch_window_viewDB.connect(self.show_db)
        self.login.close()
        self.mainClients.show()

	    


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_welcom_login_page()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()