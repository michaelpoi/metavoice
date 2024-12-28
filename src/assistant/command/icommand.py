import os
import re
import gettext
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
    def handle(self, text:str, **kwargs):
        pass

    find_patterns:dict[str, list[str]] = {}

    complied_patterns:[re.Pattern] = []

    def _compile_pattern(self, pattern:str) -> re.Pattern:
        def replace_placeholder(match):
            var_name = match.group(1)
            var_type = match.group(2) or r"\w+"  # Default to matching words
            return f"(?P<{var_name}>{var_type})"

        regex = re.sub(r"{(\w+)(?::([^}]+))?}", replace_placeholder, pattern)
        return re.compile(regex, re.IGNORECASE)



    def helper(self) -> str:
        return 'Undocumented'

    def get_find_patterns(self) -> dict[str, list[str]]|None:
        patterns =  self.find_patterns
        if not patterns:
            return None
        if isinstance(patterns, str):
            return {settings.input_language: [patterns]}
        elif isinstance(patterns, list):
            return {settings.input_language: patterns}
        else:
            return patterns

    def find_regex(self, text:str):
        if not self.complied_patterns:
            active_patterns = self.get_find_patterns()
            if not active_patterns:
                return None
            language_patterns = active_patterns[settings.input_language]
            self.complied_patterns = [self._compile_pattern(pattern) for pattern in language_patterns]

        for pattern in self.complied_patterns:
            match = pattern.search(text)
            if match:
                return match.groupdict()
        return None

    def respond(self, response:str):
        if not settings.debug:
            speaker = Speaker()
            speaker.speak(response)
        else:
            print(response)

        return response


