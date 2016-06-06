from PyQt4 import QtCore, QtGui
from functools import partial
from algorithm.frontend.iconassignment.OptionIcon import OptionIcon


class OptionView:
    # Defining Scroll Area and Scroll Layout
    def __init__(self, option_container):
        self.scroll_content = QtGui.QWidget(option_container)
        self.option_container = option_container

    def display_options(self, option_icon_path, option_callback):
        # option_path =
        item_count = len(option_icon_path)
        option_per_row = 4
        column = 0
        row = 0
        scroll_layout = QtGui.QGridLayout(self.scroll_content)
        self.scroll_content.setLayout(scroll_layout)

        def button_clicked(callback_num):
            option_callback[callback_num]()

        # Loop for Button File Assignment
        for i in range(0, item_count):
            if row == option_per_row:
                row -= option_per_row
                column += 1

            # Defining Label and Button
            option_button = QtGui.QPushButton()

            option_button.clicked.connect(partial(button_clicked, i))

            # Getting Correct Icons to Display on Button
            icons_class = OptionIcon()
            icon = icons_class.load_icons(option_icon_path[i])

            # Button Preferences
            option_button.setIconSize(QtCore.QSize(50, 50))
            option_button.setFocusPolicy(QtCore.Qt.NoFocus)
            option_button.setIcon(QtGui.QIcon(icon))

            # Putting Button and Label in Layout
            scroll_item_layout = QtGui.QVBoxLayout()
            scroll_item_layout.addWidget(option_button)

            scroll_layout.addLayout(scroll_item_layout, column, row)
            row += 1
        # Displaying Scroll Content on Scroll Area
        self.option_container.setWidget(self.scroll_content)
