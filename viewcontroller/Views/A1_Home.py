import os
from importlib import import_module

from PyQt4 import QtCore, QtGui, uic
from viewcontroller.Widgets.A1_Stack_Widget import A1_Stack_Widget

#Importing UI
path=os.path.dirname(os.path.abspath(__file__))
MainWindowUI,MainWindowBase= uic.loadUiType(os.path.join(path,'UI/mainwindow.ui'))


class A1_Home(MainWindowBase, MainWindowUI):
    def __init__(self,stack):
        """

        :param parent:
        :return:
        """

        super(A1_Home, self).__init__()



        #Makes Canvas Fullscreen
        self.showMaximized()

        #Launches Canvas from mainwindow.ui
        self.setupUi(self)
        #stack = A1_Stack_Widget()

        #Binding Search Icon click to searchMenu for all
        self.search.clicked.connect(stack.goSearch)
        #Binding Search Icon click to searchMenu for Projects
        self.projects.clicked.connect(lambda event: self.projectsMenu())

        #Starts Time

        #self.timeupdate=QtCore.QTimer(self)
        #self.timeupdate.setInterval(1000)
        #self.timeupdate.timeout.connect(self.displayTime)
        #self.timeupdate.start()




    """

    def searchMenu(self):

        #Launches Search Action

        #A1_Search(main_directory, "files/search/", "viewcontroller.A1_Spotlight", "A1_Spotlight")
        module = import_module("viewcontroller.A1_Spotlight")
        class_= getattr(module,'A1_Spotlight')
        instance=class_('files/search/')
        self.setCentralWidget(instance)

    def projectsMenu(self,main_directory):

        A1_Search(main_directory, "files/search/", "viewcontroller.A1_Projects", "A1_Projects")

    def displayTime(self):
        #Time Label

        self.timeLabel.setText(QtCore.QTime.currentTime().toString("h:mm:ss ap"))

    """