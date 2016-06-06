from model.data.plugin.OptionLabel import OptionLabel


class IPlugin:
    def __init__(self, info_container):
        self.infoContainer = info_container
        self.label = OptionLabel("icon", "placeholder")

    def option_button_pressed(self):
        raise NotImplementedError("Not implemented")
