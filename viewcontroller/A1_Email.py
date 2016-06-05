import os

from PyQt4 import QtCore, QtGui, uic
import sys


#Importing UI
path=os.path.dirname(os.path.abspath(__file__))
EmailWindowUI,EmailWindowBase= uic.loadUiType(os.path.join(path,'UI/email.ui'))


class EmailWindow(EmailWindowBase,EmailWindowUI):
    def __init__(self):
        """

        :param parent:
        :return:
        """

        EmailWindowBase.__init__(self)
        #super(EmailWindow,self).__init__(parent)



        self.setupUi(self)

