import os

from assistant.command.icommand import ICommand
from assistant.manager import CommandManager
from assistant.core.i18n import _


class Helper(ICommand):
    def helper(self) -> str:
        return _("Write help to see documentation")

    find_patterns = ['help', 'помощь']

    def handle(self, text:str):
        response = '| Name | Triggers | Docs |\n'
        for name, doc in CommandManager.helper().items():
            response += f'| {name} | {doc["triggers"]} | {doc["docs"]} |\n'

        return response