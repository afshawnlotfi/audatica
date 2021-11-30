from algorithm.backend.PluginLoader import PluginLoader
from algorithm.frontend.frameview.FileInfoView import FileInfoView
from algorithm.frontend.frameview.OptionView import OptionView


class OptionManager:
    def __init__(self, info_container, options_container):
        self.info_container = info_container
        self.options_container = options_container
        self.plugin_loader = PluginLoader()
        plugin_list = self.plugin_loader.load_all_plugins(info_container=self.info_container)
        option_icon_path = []
        option_callback = []
        for plugin in plugin_list:
            option_icon = plugin.exports["button_icon"]
            option_icon_path.append(option_icon)
            activated_callback = plugin.exports["callbacks"]["activate"]
            option_callback.append(activated_callback)

        option_view = OptionView(options_container)
        option_view.display_options(option_icon_path, option_callback)

    def display_frame(self, file_view_container, file_path):
        info_view = FileInfoView()
        info_view.display_info(file_view_container, file_path)
