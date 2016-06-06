import os


class Delete:
    def __init__(self, path, filename):
        os.system("rm -rf %s%s" % (path, filename))
