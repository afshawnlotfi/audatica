import os

import imp

PluginFolder = "./plugins"
MainModule = "Plugin"


class PluginLoader:
    def __init__(self):
        self._pluginList = {}
        possible_plugins = os.listdir(PluginFolder)
        for i in possible_plugins:
            location = os.path.join(PluginFolder, i)
            if not os.path.isdir(location) or not MainModule + ".py" in os.listdir(location):
                continue
            info = imp.find_module(MainModule, [location])
            self._pluginList[i] = {
                "info": info,
                "loaded": False
            }

    def get_plugin_list(self):
        return self._pluginList

    def load_plugin(self, name):
        if self._pluginList.has_key(name):
            module = imp.load_module(MainModule, *self._pluginList[name]["info"])
            self._pluginList[name]['loaded'] = True
            return module
        return None

    def load_all_plugins(self):
        for key, value in self._pluginList.iteritems():
            if value['loaded'] is False:
                pass
