from PyQt4 import QtCore, QtGui
from functools import partial

from algorithm.frontend.iconassignment.SearchIcon import SearchIcon


# from algorithm.backend.OptionManager import OptionManager
class SearchView:
    # Defining Scroll Area and Scroll Layout
    def __init__(self, file_scroll):
        self.scroll_content = QtGui.QWidget(file_scroll)
        self.file_scroll = file_scroll

    def display_files(self, file_list, file_path, button_callback):
        item_count = len(file_list)

        file_per_row = 3
        column = 0
        row = 0
        scroll_layout = QtGui.QGridLayout(self.scroll_content)
        self.scroll_content.setLayout(scroll_layout)
        # Loop for Button File Assignment
        for i in range(0, item_count):
            if row == file_per_row:
                row -= file_per_row
                column += 1

            # Defining Label and Button
            file_button = QtGui.QPushButton()

            # file_button.clicked.connect(lambda z=i: callback(file_order[z]))
            file_button.clicked.connect(partial(button_callback, file_list[i]))
            file_label = QtGui.QPushButton(file_list[i])

            # Getting Correct Icons to Display on Button
            icons_class = SearchIcon()
            icon = icons_class.load_icons(file_path + file_list[i])

            # Button Preferences
            file_button.setIconSize(QtCore.QSize(190, 190))
            file_button.setFocusPolicy(QtCore.Qt.NoFocus)
            file_label.setFocusPolicy(QtCore.Qt.NoFocus)
            file_button.setIcon(QtGui.QIcon(icon))
            file_label.setStyleSheet('''
            color: rgba(255, 255, 255, 180);
            ''')

            # Putting Button and Label in Layout
            scroll_item_layout = QtGui.QVBoxLayout()
            scroll_item_layout.addWidget(file_button)
            scroll_item_layout.addWidget(file_label)

            scroll_layout.addLayout(scroll_item_layout, column, row)
            row += 1
        # Displaying Scroll Content on Scroll Area
        self.file_scroll.setWidget(self.scroll_content)
