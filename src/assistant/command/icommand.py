from assistant.speaker import Speaker
from assistant.settings.default_settings import settings


class CommandMeta(type):
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            command_instance = cls()
            cls.registry[name] = command_instance

        super().__init__(name, bases, attrs)

class ICommand(metaclass=CommandMeta):
    def handle(self, text:str):
        pass

    find_patterns:list[str] = []

    def helper(self) -> str:
        return 'Undocumented'

    def find(self, text:str):
        for pattern in self.find_patterns:
            if pattern in text:
                return True

        return False

    def respond(self, response:str):
        if not settings.debug:
            speaker = Speaker()
            speaker.speak(response)
        else:
            print(response)

        return response


