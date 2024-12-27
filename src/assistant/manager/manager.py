from assistant.command.icommand import ICommand
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
            if command.find(pattern):
                return command.handle(pattern)
        raise ValueError('Command not found')

    @staticmethod
    def helper():
        documentation_dict = {}
        for name, command in CommandManager.show().items():
            documentation_dict[name] = {"triggers": command.find_patterns,
                                        "docs":command.helper()}

        return documentation_dict