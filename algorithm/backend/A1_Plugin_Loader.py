import os

import imp

PluginFolder = "./plugins"
MainModule = "Plugin"


class A1_Plugin_Loader:
    def __init__(self):
        self._pluginList = {}
        possibleplugins = os.listdir(PluginFolder)
        for i in possibleplugins:
            location = os.path.join(PluginFolder, i)
            if not os.path.isdir(location) or not MainModule + ".py" in os.listdir(location):
                continue
            info = imp.find_module(MainModule, [location])
            self._pluginList[i] = {
                "info": info,
                "loaded": False
            }

    def getPluginList(self):
        return self._pluginList

    def loadPlugin(self, name):
        if self._pluginList.has_key(name):
            module = imp.load_module(MainModule, *self._pluginList[name]["info"])
            self._pluginList[name]['loaded'] = True
            return module
        return None

    def loadAllPlugins(self):
        for key, value in self._pluginList.iteritems():
            if value['loaded'] is False:
                plugin = self.loadPlugin(key)