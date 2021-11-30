import os

from PyQt4 import uic

# Importing UI
path = os.path.dirname(os.path.abspath(__file__))
MainWindowUI, MainWindowBase = uic.loadUiType(os.path.join(path, 'UI/mainwindow.ui'))


class HomeWindow(MainWindowBase, MainWindowUI):
    def __init__(self, stack):
        super(HomeWindow, self).__init__()

        # Makes Canvas full screen
        self.showMaximized()

        # Launches Canvas from UI
        self.setupUi(self)
        # stack = StackWidget()

        # Binding search Icon click to searchMenu for all
        self.search.clicked.connect(stack.go_search)
        # Binding search Icon click to searchMenu for Projects
        self.projects.clicked.connect(lambda event: self.projectsMenu())

        # Starts Time

        # self.time_update=QtCore.QTimer(self)
        # self.time_update.setInterval(1000)
        # self.time_update.timeout.connect(self.displayTime)
        # self.time_update.start()

