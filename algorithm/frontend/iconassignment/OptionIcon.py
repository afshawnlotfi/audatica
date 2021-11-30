from PyQt4 import QtGui


class OptionIcon:
    def __init__(self):
        pass

    def load_icons(self, option_icon_path):
        global icon

        icon = QtGui.QPixmap(option_icon_path)

        return icon
