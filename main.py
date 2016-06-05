
import sys
import os
from PyQt4 import QtCore, QtGui, uic
import icons_rc





if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)


    from viewcontroller.A1_Home import A1_Home

    login_window=A1_Home(os.path.dirname(os.path.abspath(__file__)) + '/')
    login_window.show()
    sys.exit(app.exec_())


