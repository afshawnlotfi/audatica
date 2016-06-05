import os


class Delete():
    def __init__(self,path,file):
        os.system("rm -rf %s%s"%(path,file))
class Launch():
    def __init__(self,application,path,file):
        os.system("%s %s%s"%(application,path,file))
