from algorithm.frontend.frameview.InfoView import InfoView


class Option:
    def __init__(self):
        pass

    def display_frame(self, file_view_container, file, path):
        info_view = InfoView()
        info_view.display_info(file_view_container, file, path)
