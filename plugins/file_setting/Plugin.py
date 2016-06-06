class Plugin:
    def __init__(self, *args, **kwargs):
        if kwargs.has_key("info_container"):
            self.info_container = kwargs["info_container"]
        self.exports = {
            "button_icon": "/home/audatica/PycharmProjects/audatica1-ui/plugins/file_setting/icons/setting.png",
            "callbacks": {
                "activate": self.activated  # activate callback calls when the button for this plugin has been pressed
            }
        }

    def activated(self):
        print('yo1')
