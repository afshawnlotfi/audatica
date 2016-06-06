from PyQt4 import QtCore, QtGui

from algorithm.backend.ItemInfo import ItemInfo


class FileInfoFrame:
    # Displaying frame settings
    def __init__(self):
        pass

    def display_frame(self, file_path):

        scroll_item_layout = QtGui.QVBoxLayout()
        scroll_height = 420
        info_class = ItemInfo()
        icon, filename, file_size, created, modified = info_class.file_information(file_path)

        file_icon = {"item": QtGui.QPushButton()}
        file_icon["item"].setIconSize(QtCore.QSize(230, 230))
        file_icon["item"].setIcon(QtGui.QIcon(icon))

        file_title = {"item": QtGui.QLabel(filename), "size": 15}
        file_size = {"item": QtGui.QLabel(file_size), "size": 10}
        file_modified = {"item": QtGui.QLabel(modified), "size": 11}
        file_created = {"item": QtGui.QLabel(created), "size": 11}

        all_items = [file_icon, file_title, file_size, file_modified, file_created]
        text_items = [file_title, file_size, file_modified, file_created]

        for t in range(0, len(text_items)):
            text_items[t]["item"].setStyleSheet('''
            color: rgba(255, 255, 255, 180);
            font: %spt "Ubuntu";
            ''' % text_items[t]["size"])
            text_items[t]["item"].setAlignment(QtCore.Qt.AlignCenter)

        for a in range(0, len(all_items)):
            scroll_item_layout.addWidget(all_items[a]["item"])

        return scroll_item_layout, scroll_height

    # Displaying option settings
    def display_option(self):
        pass
