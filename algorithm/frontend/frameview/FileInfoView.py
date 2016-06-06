from PyQt4 import QtCore, QtGui

from viewcontroller.options.built_in.File_Home.FileInfoFrame import FileInfoFrame


class FileInfoView:
    def __init__(self):
        pass

    def display_info(self, info_scroll, file_path):
        option_class = FileInfoFrame()
        scroll_item_layout, scroll_height = option_class.display_frame(file_path)
        if scroll_height > 500:
            scroll_height = 500
        info_scroll.setGeometry(QtCore.QRect(1110, 120, 330, scroll_height))
        scroll_content = QtGui.QWidget(info_scroll)
        scroll_layout = QtGui.QVBoxLayout(scroll_content)
        scroll_content.setLayout(scroll_layout)

        scroll_layout.addLayout(scroll_item_layout)
        info_scroll.setWidget(scroll_content)
