import os
import time
from algorithm.frontend.A1_Icons.A1_Search_Icon import Search_Icons
class A1_Item_Info():

    def file_information(self,file,path):
        '''

        :param file: file to gather information
        :param path: path to file
        :return:
        '''



        check_dir=os.path.isdir(path + file)
        #Finding file icon
        icons_class=Search_Icons()
        icon=icons_class.load_icons(path,file)

        #Looks up item size
        filesize = "%.2f MB"%(os.path.getsize(path+ file)/float(1000000))
        #Looks up the date of Modification
        modified = "Modified: %s"%time.strftime('%B %d,%Y at %l:%M %p',time.localtime(os.path.getmtime(path+file)))

        #Looks up the date of Creation
        created = "Created: %s"%time.strftime('%B %d,%Y at %l:%M %p',time.localtime(os.path.getctime(path+file)))

        #Displays in respective icons display

        return icon,file,filesize,created,modified


