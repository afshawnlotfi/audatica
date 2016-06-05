from PyQt4 import QtCore, QtGui
import imghdr
import os

class Search_Icons():
    def load_icons(self,path,file):
        '''

        :param path: path to file
        :param file: file to initialize icon
        :return:
        '''

        check_dir=os.path.isdir(path+file)
        if str(check_dir)=="False":
            file_type=str(imghdr.what(path+file))
            if file_type=="None":
                icon = QtGui.QPixmap(":/icons/file.png")
            else:
                icon = QtGui.QPixmap(path+file)
        elif str(check_dir)=="True":
                icon = QtGui.QPixmap(path+file+"/%s.jpg"%file)
        return icon