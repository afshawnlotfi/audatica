import os


class Search:
    def __init__(self, directory):
        # Sorts File by Alphabet
        self.file_sort = sorted(os.listdir(directory))

    def search(self, search_string):
        # Organizing files that start with keyword
        file_order = [s for s in self.file_sort if s.startswith(search_string)]

        return file_order
