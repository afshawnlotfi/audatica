from PyQt4.QtCore import QTimeLine
from PyQt4.QtGui import *


class Fade(QWidget):
    def __init__(self, old_object, new_object, delay):
        QWidget.__init__(self, new_object)

        self.old_pix_map = QPixmap(new_object.size())
        old_object.render(self.old_pix_map)
        self.pix_map_opacity = 1.0

        self.time_line = QTimeLine()
        self.time_line.valueChanged.connect(self.fade)
        self.time_line.finished.connect(self.close)
        self.time_line.setDuration(delay)
        self.time_line.start()

        self.resize(new_object.size())
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setOpacity(self.pix_map_opacity)
        painter.drawPixmap(0, 0, self.old_pix_map)
        painter.end()

    def fade(self, value):
        self.pix_map_opacity = 1.0 - value
        self.repaint()
