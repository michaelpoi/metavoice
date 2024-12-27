import json

from assistant.manager import CommandManager
from assistant.listener import record_audio, recognize_speech, get_voice_input
from assistant.settings.default_settings import settings


class Assistant:
    def __init__(self):
        pass

    def debug_server(self):
        while True:
            text = input("Your speech: ")
            if text:
                CommandManager.find_and_execute(text)

    def production_server(self):
        while True:
            text = get_voice_input()
            if text:
                self.process_command(text)

    def process_command(self, text):
        try:
            return CommandManager.find_and_execute(text)
        except ValueError as e:
            print(e)
            return "Command not found"

    def load_modules(self):
        CommandManager.load_commands(settings)

    def serve(self):
        self.load_modules()
        print(CommandManager.show())
        if settings.debug:
            self.debug_server()

        self.production_server()

