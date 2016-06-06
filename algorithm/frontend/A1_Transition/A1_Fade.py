from PyQt4.QtCore import QTimeLine
from PyQt4.QtGui import *

class A1_Fade(QWidget):

    def __init__(self, old_object, new_object, delay):

        QWidget.__init__(self, new_object)

        self.old_pixmap = QPixmap(new_object.size())
        old_object.render(self.old_pixmap)
        self.pixmap_opacity = 1.0

        self.timeline = QTimeLine()
        self.timeline.valueChanged.connect(self.fade)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(delay)
        self.timeline.start()

        self.resize(new_object.size())
        self.show()

    def paintEvent(self, event):

        painter = QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.old_pixmap)
        painter.end()

    def fade(self, value):

        self.pixmap_opacity = 1.0 - value
        self.repaint()