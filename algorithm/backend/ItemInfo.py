import os
import time
from algorithm.frontend.iconassignment.SearchIcon import SearchIcon
import ntpath

class ItemInfo:
    def __init__(self):
        pass

    def file_information(self, file_path):

        file_name = ntpath.basename(file_path)

        # Finding file icon
        icons_class = SearchIcon()
        icon = icons_class.load_icons(file_path)

        # Looks up item size
        file_size = "%.2f MB" % (os.path.getsize(file_path) / float(1000000))
        # Looks up the date of Modification
        modified = "Modified: %s" % time.strftime('%B %d,%Y at %l:%M %p',
                                                  time.localtime(os.path.getmtime(file_path)))

        # Looks up the date of Creation
        created = "Created: %s" % time.strftime('%B %d,%Y at %l:%M %p',
                                                time.localtime(os.path.getctime(file_path)))

        # Displays in respective icons display

        return icon, file_name, file_size, created, modified
