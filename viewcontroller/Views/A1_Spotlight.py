import os
import sys
from PyQt4 import QtCore, QtGui, uic

from algorithm.backend.A1_Option import A1_Option
from algorithm.backend.search.A1_Search import A1_Search
from algorithm.frontend.A1_View.A1_Search_View import A1_Search_View

path = os.path.dirname(os.path.abspath(__file__))
SpotlightWindowUI, SpotlightWindowBase = uic.loadUiType(os.path.join(path, 'UI/spotlight.ui'))


class A1_Spotlight(SpotlightWindowBase, SpotlightWindowUI):
    def __init__(self, stack, directory):
        '''

        :param main_directory: main directory
        :param dir_search: directory to search
        :return:
        '''
        super(A1_Spotlight, self).__init__()

        self.directory = directory

        # Makes Canvas Fullscreen
        self.showMaximized()

        # Launches Canvas from search.ui
        self.setupUi(self)

        # Importing A1_Search to send text to from text widget
        self.close.clicked.connect(stack.goHome)

        self.searchwin = A1_Search

        # Gathering items from ui and exporting to A1_Search


        def textChanged():
            file_amount, file_order = searcher.search(self.searchEntry.text())
            self.updateSearchUi(self.directory, file_amount, file_order)

        searcher = A1_Search(self.directory)
        textChanged()

        # Launching Search Action and connecting it to keystroke
        # self.searchwin.searchAction(self,,self.file_scroll,self.info_scroll,dir_search)

        self.searchEntry.textChanged.connect(lambda event: textChanged())

    def updateSearchUi(self, directory, file_amount, file_order):
        file = ""

        if (len(file_order) > 0):
            file = file_order[0]
        view_files = A1_Search_View(self.file_scroll)

        def buttonPressed(newFile):
            option_class = A1_Option()
            option_class.display_frame(self.info_scroll, newFile, self.directory)

        view_files.display_files(file_amount, file_order, directory, buttonPressed)

        buttonPressed(file)
