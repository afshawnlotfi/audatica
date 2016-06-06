from model.data.plugin.OptionLabel import OptionLabel


class IPlugin:
    def __init__(self, infoContainer):
        self.infoContainer = infoContainer
        self.label = OptionLabel("icon", "placeholder")

    def buttonPressed(self):
        raise NotImplementedError("Not implemented")