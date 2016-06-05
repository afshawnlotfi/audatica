import os

from PyQt4 import QtCore, QtGui, uic
from algorithm.backend.A1_Search import A1_Search

#Importing UI
path=os.path.dirname(os.path.abspath(__file__))
MainWindowUI,MainWindowBase= uic.loadUiType(os.path.join(path,'UI/mainwindow.ui'))


class A1_Home(MainWindowBase, MainWindowUI):
    def __init__(self,main_directory):
        """

        :param parent:
        :return:
        """

        super(A1_Home, self).__init__()



        #Makes Canvas Fullscreen
        self.showMaximized()

        #Launches Canvas from mainwindow.ui
        self.setupUi(self)

        #Binding Search Icon click to searchMenu for all
        self.search.clicked.connect(lambda event: self.searchMenu(main_directory))
        #Binding Search Icon click to searchMenu for Projects
        self.projects.clicked.connect(lambda event: self.projectsMenu(main_directory))

        #Starts Time

        self.timeupdate=QtCore.QTimer(self)
        self.timeupdate.setInterval(1000)
        self.timeupdate.timeout.connect(self.displayTime)
        self.timeupdate.start()
        self.search_tag=0






    def searchMenu(self,main_directory):
        """
        Function that launches Search UI
        :return:
        """
        #Launches Search Action

        A1_Search(main_directory, "files/search/", "viewcontroller.A1_Spotlight", "A1_Spotlight")


    def projectsMenu(self,main_directory):

        A1_Search(main_directory, "files/search/", "viewcontroller.A1_Projects", "A1_Projects")

    def displayTime(self):
        #Time Label

        self.timeLabel.setText(QtCore.QTime.currentTime().toString("h:mm:ss ap"))

