from PyQt4 import QtCore, QtGui, uic
from viewcontroller.Options.Built_In.File_Home.File_Info_Frame import File_Info_Frame


class A1_Info_View():
    def display_info(self, info_scroll, file, path):
        '''

        :param item_icon: Icon Display
        :param item_title: Title Display
        :param item_subtitle: Subtitle Dispaly
        :param item_info1: Additional Information 1
        :param item_info2: Additional Information 2
        :return:
        '''

        # path,module,class_run=dir_search,import_list['module'],import_list['class']


        # module = import_module(module)
        # class_= getattr(module,class_run)
        # instance=class_

        option_class = File_Info_Frame()
        scroll_item_layout, scroll_height = option_class.display_frame(file, path)
        if scroll_height > 500:
            scroll_height = 500
        info_scroll.setGeometry(QtCore.QRect(1110, 120, 330, scroll_height))
        scroll_content = QtGui.QWidget(info_scroll)
        scroll_layout = QtGui.QVBoxLayout(scroll_content)
        scroll_content.setLayout(scroll_layout)

        scroll_layout.addLayout(scroll_item_layout)
        info_scroll.setWidget(scroll_content)
