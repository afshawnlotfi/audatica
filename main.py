import sys
from PyQt4 import QtGui

from PyQt4.QtGui import *
#Test
from viewcontroller.views.HomeWindow import HomeWindow
from viewcontroller.views.SpotlightWindow import SpotlightWindow
from viewcontroller.widgets.StackWidget import StackWidget

# Main function -- called when the application starts
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    A1_Window = QWidget()

    # Importing stack widget
    stack = StackWidget()
    # Importing views
    # login_window = LoginWindow(stack)
    home_window = HomeWindow(stack)
    spotlight_window = SpotlightWindow(stack, "files/search/")

    # Adding views to stack widget
    # stack.addWidget(login_window)
    stack.addWidget(home_window)
    stack.addWidget(spotlight_window)

    stack.show()

    sys.exit(app.exec_())
