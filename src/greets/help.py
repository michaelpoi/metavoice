from assistant.command.icommand import ICommand
from assistant.manager import CommandManager

class Helper(ICommand):
    def helper(self) -> str:
        return "Write help to see documentation"

    find_patterns = ['help', 'помощь']

    def handle(self, text:str):
        response = '| Name | Triggers | Docs |\n'
        for name, doc in CommandManager.helper().items():
            response += f'| {name} | {doc["triggers"]} | {doc["docs"]} |\n'

        return response