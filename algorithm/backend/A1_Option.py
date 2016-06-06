#from viewcontroller.Options.Built_In.Option_Frames.file_info import file_info
from algorithm.frontend.A1_View.A1_Info_View import A1_Info_View
class A1_Option():
    def display_frame(self,file_scroll,file,path):

        infoview_class=A1_Info_View()
        infoview_class.display_info(file_scroll,file,path)


