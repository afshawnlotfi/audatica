import os
from algorithm.backend.A1_Search import A1_Search
from PyQt4 import QtCore, QtGui, uic
import time

#Importing UI
path=os.path.dirname(os.path.abspath(__file__))
ProjectsWindowUI,ProjectsWindowBase= uic.loadUiType(os.path.join(path,'UI/projects.ui'))


class A1_Projects(ProjectsWindowBase, ProjectsWindowUI):
    def __init__(self,main_directory,dir_search):
        '''

        :param main_directory: main directory
        :param dir_search: directory to search
        :return:
        '''

        super(A1_Projects, self).__init__()
        self.showMaximized()



        self.setupUi(self)
        self.searchwin=A1_Search
        #Importing A1_Search to send text to from text widget




        #Launching Search Action and connecting it to keystroke
        #self.searchwin.searchAction(self,ui_items,import_list,item_num)
        #self.searchEntry.textChanged.connect(lambda event: self.searchwin.searchAction(self,ui_items,import_list,item_num))



