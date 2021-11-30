import os


class Launch:
    def __init__(self, application, path, filename):
        os.system("%s %s%s" % (application, path, filename))
