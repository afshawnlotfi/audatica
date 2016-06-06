import imghdr
import os
from PyQt4 import QtGui


class SearchIcon:
    def __init__(self):
        pass

    def load_icons(self, file_path):


        global icon
        check_dir = os.path.isdir(file_path)
        if str(check_dir) == "False":
            file_type = str(imghdr.what(file_path))
            if file_type == "None":
                icon = QtGui.QPixmap(":/icons/file.png")
            else:
                icon = QtGui.QPixmap(file_path)
        elif str(check_dir) == "True":
            icon = QtGui.QPixmap(file_path + "/cover.jpg")
        return icon
