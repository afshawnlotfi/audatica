import os
from importlib import import_module

PluginFolder = "/home/audatica/PycharmProjects/audatica1-ui/plugins"
MainModule = "Plugin"


class PluginLoader:
    def __init__(self):
        self._pluginList = []

        possible_plugins = os.listdir(PluginFolder)
        for i in possible_plugins:
            location = os.path.join(PluginFolder, i)
            if not os.path.isdir(location) or not MainModule + ".py" in os.listdir(location):
                continue
            self._pluginList.append(i)

    def get_plugin_list(self):
        return self._pluginList

    def load_plugin(self, name, *args, **kwargs):
        if name in self._pluginList:
            module_name = "plugins.%s.Plugin"%name
            module = import_module(module_name)
            module_class = getattr(module, "Plugin")
            return module_class(args, kwargs)
        return None

    def load_all_plugins(self, *args, **kwargs):
        list = []
        for plugin_name in self._pluginList:
            plugin = self.load_plugin(plugin_name, args, kwargs)
            if plugin is not None:
                list.append(plugin)
        return list
