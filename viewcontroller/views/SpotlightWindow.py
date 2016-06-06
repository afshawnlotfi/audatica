import os
from PyQt4 import uic

from algorithm.backend.Option import Option
from algorithm.backend.search.Search import Search
from algorithm.frontend.frameview.SearchView import SearchView

path = os.path.dirname(os.path.abspath(__file__))
SpotlightWindowUI, SpotlightWindowBase = uic.loadUiType(os.path.join(path, 'UI/spotlight.ui'))


class SpotlightWindow(SpotlightWindowBase, SpotlightWindowUI):
    def __init__(self, stack, directory):
        super(SpotlightWindow, self).__init__()

        self.directory = directory

        # Makes Canvas full screen
        self.showMaximized()

        # Launches Canvas from search.ui
        self.setupUi(self)

        # Importing search to send text to from text widget
        self.close.clicked.connect(stack.go_home)


        # Gathering items from ui and exporting to search


        def text_changed():
            file_amount, file_order = searcher.search(self.searchEntry.text())
            self.update_search_ui(self.directory, file_amount, file_order)

        searcher = Search(self.directory)
        text_changed()



        self.searchEntry.textChanged.connect(lambda event: text_changed())

    def update_search_ui(self, directory, file_amount, file_order):
        filename = ""

        if len(file_order) > 0:
            filename = file_order[0]
        view_files = SearchView(self.file_scroll)

        def file_button_pressed(new_file):
            option_class = Option()
            option_class.display_frame(self.info_scroll, new_file, self.directory)

        view_files.display_files(file_amount, file_order, directory, file_button_pressed)

        file_button_pressed(filename)
