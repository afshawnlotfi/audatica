
import os
import sys
from PyQt4.QtCore import QTimeLine
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui, uic
from viewcontroller.Views.A1_Home import A1_Home
from viewcontroller.Views.A1_Spotlight import A1_Spotlight
from viewcontroller.Widgets.A1_Stack_Widget import A1_Stack_Widget




import icons_rc





if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)


    A1_Window= QWidget()

    #Importing stack widget
    stack = A1_Stack_Widget()
    #Importing Views
    home_window=A1_Home(stack)
    spotlight_window=A1_Spotlight(stack,"files/search/")

    #Adding Views to stack widget
    stack.addWidget(home_window)
    stack.addWidget(spotlight_window)






    stack.show()

    sys.exit(app.exec_())





