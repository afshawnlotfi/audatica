

class Option_Icons():
    def init_icon(self,icon_list):
        #Initilizing Icons

        icon_dictionary={}
        for i in range (0,len(icon_list)):
            exec("icon_dictionary['%s']=QtGui.QIcon(QtGui.QPixmap(':/icons/%s.png'))"%(icon_list[i],icon_list[i]))
        return icon_dictionary