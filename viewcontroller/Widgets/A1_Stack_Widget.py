from PyQt4.QtCore import QTimeLine
from PyQt4.QtGui import *
class A1_Stack_Widget(QStackedWidget):

    def __init__(self, parent = None):
        QStackedWidget.__init__(self, parent)
        self.showMaximized()
    def setindex(self, index):
        from algorithm.frontend.A1_Transition.A1_Fade import A1_Fade
        A1_Fade(self.currentWidget(), self.widget(index),500)
        QStackedWidget.setCurrentIndex(self, index)

    def goHome(self):
        self.setindex(0)

    def goSearch(self):
        self.setindex(1)