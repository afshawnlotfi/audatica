import os
from PyQt4 import uic

# Importing UI
path = os.path.dirname(os.path.abspath(__file__))
ProjectsWindowUI, ProjectsWindowBase = uic.loadUiType(os.path.join(path, 'UI/projects.ui'))


class ProjectsWindow(ProjectsWindowBase, ProjectsWindowUI):
    def __init__(self):
        """

        :return:
        """

        super(ProjectsWindow, self).__init__()
        self.showMaximized()

        self.setupUi(self)
        # Importing search to send text to from text widget




        # Launching search Action and connecting it to keystroke
