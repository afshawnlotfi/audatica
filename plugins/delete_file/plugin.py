from model.data.plugin.IPlugin import IPlugin


class Plugin(IPlugin):
    def __init__(self, infoContainer):
        IPlugin.__init__(self, infoContainer)

    def buttonPressed(self):
        pass
