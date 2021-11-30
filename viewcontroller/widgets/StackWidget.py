from PyQt4.QtGui import *


class StackWidget(QStackedWidget):
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent)
        self.showMaximized()

    def set_index(self, index):
        from algorithm.frontend.transitions.Fade import Fade
        Fade(self.currentWidget(), self.widget(index), 500)
        QStackedWidget.setCurrentIndex(self, index)

    def go_home(self):
        self.set_index(0)

    def go_search(self):
        self.set_index(1)
