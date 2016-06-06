import imghdr
import os
from PyQt4 import QtGui


class SearchIcons:
    def __init__(self):
        pass

    def load_icons(self, path, filename):
        """

        :param path: path to file
        :param filename: file to initialize icon
        :return:
        """

        global icon
        check_dir = os.path.isdir(path + filename)
        if str(check_dir) == "False":
            file_type = str(imghdr.what(path + filename))
            if file_type == "None":
                icon = QtGui.QPixmap(":/icons/file.png")
            else:
                icon = QtGui.QPixmap(path + filename)
        elif str(check_dir) == "True":
            icon = QtGui.QPixmap(path + filename + "/%s.jpg" % filename)
        return icon
