import fnmatch
import os

from algorithm.backend.A1_Option import A1_Option
from algorithm.frontend.A1_View.A1_Search_View import A1_Search_View


class A1_Search:
    def __init__(self, directory):
        self.directory = directory

    def search(self, searchString):
        configfiles = [os.path.join(dirpath, f)
                       for dirpath, dirnames, files in os.walk(self.directory)
                       for f in fnmatch.filter(files, '*.txt')]



        #Sorts File by Alphabet
        self.file_sort = sorted(os.listdir(self.directory))
        #Organizing files that start with keyword
        file_order = [s for s in self.file_sort if s.startswith(searchString)]
        file_amount = len(file_order)
        #Num_count is how much the Search should display out of 12
        return file_amount,file_order


