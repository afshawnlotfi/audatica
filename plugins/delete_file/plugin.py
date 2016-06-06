from model.data.plugin.IPlugin import IPlugin


class Plugin(IPlugin):
    def __init__(self, info_container):
        IPlugin.__init__(self, info_container)

    def option_button_pressed(self):
        pass
