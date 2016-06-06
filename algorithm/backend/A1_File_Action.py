import os


class Delete:
    def __init__(self, path, filename):
        os.system("rm -rf %s%s" % (path, filename))


class Launch:
    def __init__(self, application, path, filename):
        os.system("%s %s%s" % (application, path, filename))
