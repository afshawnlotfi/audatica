import os
import time
from algorithm.frontend.iconassignment.SearchIcon import SearchIcons


class ItemInfo:
    def __init__(self):
        pass

    def file_information(self, filename, path):
        """

        :param filename: file to gather information
        :param path: path to file
        :return:
        """

        # Finding file icon
        icons_class = SearchIcons()
        icon = icons_class.load_icons(path, filename)

        # Looks up item size
        file_size = "%.2f MB" % (os.path.getsize(path + filename) / float(1000000))
        # Looks up the date of Modification
        modified = "Modified: %s" % time.strftime('%B %d,%Y at %l:%M %p',
                                                  time.localtime(os.path.getmtime(path + filename)))

        # Looks up the date of Creation
        created = "Created: %s" % time.strftime('%B %d,%Y at %l:%M %p',
                                                time.localtime(os.path.getctime(path + filename)))

        # Displays in respective icons display

        return icon, filename, file_size, created, modified
