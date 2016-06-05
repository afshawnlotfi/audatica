import os
import fnmatch
from importlib import import_module
from algorithm.frontend.A1_Search_View import A1_Search_View
from algorithm.backend.A1_Option import A1_Option
class A1_Search():
    def __init__(self,main_directory,dir_search,module,class_run):

        '''

        :param main_directory: main directory path
        :param dir_search: directory to search
        :param module: module using search algorithm
        :param class_run: class within module using search
        :return:
        '''

        #import specific module that uses Search
        module = import_module(module)
        class_= getattr(module,class_run)
        instance=class_(main_directory,dir_search)

        instance.show()

    @staticmethod
    def searchAction(self,search_entry,file_scroll,info_scroll,dir_search):
        '''

        :param self:
        :param search_entry: search entry that is being searched
        :param import_list: importing disctionary of module calling search {'main_directory'':,'module'':,'class':''}
        :param dir_search: what directory to search
        :param item_max: maximum number of items to display in search
        :param file_scroll: scroll item
        :param file_per_row: number of items per row
        :return:
        '''





        key_in=search_entry.text()
        configfiles = [os.path.join(dirpath, f)
                       for dirpath, dirnames, files in os.walk(dir_search)
                       for f in fnmatch.filter(files, '*.txt')]



        #Sorts File by Alphabet
        self.file_sort = sorted(os.listdir(dir_search))
        #Organizing files that start with keyword
        file_order = [s for s in self.file_sort if s.startswith(key_in)]
        file_amount = len(file_order)
        #Num_count is how much the Search should display out of 12


        try:
            view_files=A1_Search_View(file_scroll)

            view_files.display_files(file_amount,file_order,dir_search)

            option_class=A1_Option()
            option_class.display_frame(info_scroll,file_order[0],dir_search)
        except Exception:
            pass




