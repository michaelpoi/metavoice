from assistant.command.icommand import ICommand
from assistant.settings.default_settings import settings
import importlib

class CommandManager:
    @staticmethod
    def show():
        return ICommand.registry

    @staticmethod
    def load_commands(settings):
        for setting in getattr(settings, 'modules'):
            importlib.import_module(setting)

    @staticmethod
    def find_and_execute(pattern):
        for name,command in CommandManager.show().items():
            if (var_dict := command.find_regex(pattern)) is not None:
                return command.handle(pattern, **var_dict)
        raise ValueError('Command not found')

    @staticmethod
    def helper():
        documentation_dict = {}
        for name, command in CommandManager.show().items():
            documentation_dict[name] = {"triggers": command.get_find_patterns()[settings.input_language],
                                        "docs":command.helper()}

        return documentation_dict