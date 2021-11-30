import os
from importlib import import_module

PluginFolder = os.getcwd() +  "/plugins"
MainModule = "Plugin"


class PluginLoader:
    def __init__(self):
        self._pluginList = []

        possible_plugins = os.listdir(PluginFolder)
        for i in possible_plugins:
            location = os.path.join(PluginFolder, i)
            if not os.path.isdir(location) or not MainModule + ".py" in os.listdir(location):
                continue
            #Ordering List with priority
            # mylist=['a','b','c','d','e']
            # myorder=[3,2,0,1,4]
            # mylist = [ mylist[i] for i in myorder]
            print i
            self._pluginList.append(i)

    def get_plugin_list(self):
        return self._pluginList

    def load_plugin(self, name, *args, **kwargs):
        if name in self._pluginList:
            module_name = "plugins.%s.Plugin" % name
            module = import_module(module_name)
            module_class = getattr(module, "Plugin")
            return module_class(args, kwargs)
        return None

    def load_all_plugins(self, *args, **kwargs):
        plugin_list = []
        for plugin_name in self._pluginList:
            plugin = self.load_plugin(plugin_name, args, kwargs)
            if plugin is not None:
                plugin_list.append(plugin)
        return plugin_list
