from assistant.command.icommand import ICommand
from assistant.predefined.responses import done_responses, error_responses
from assistant.settings.default_settings import settings
import uuid

class WriteCommand(ICommand):
    find_patterns = ['write', 'напиши']

    def write(self, filename, content):
        try:
            with open(settings.write_location / filename, 'w+') as f:
                f.write(content)
            self.respond(done_responses())
        except Exception as e:
            self.respond(f"{error_responses()} {str(e)}")

    def handle(self, text):
        if text.count('as'):
            parts = text.split(' as ')
            content = parts[0][len('write '):]
            filename = parts[1] + '.txt'
            self.write(filename, content)

        else:
            filename = str(uuid.uuid4()) + '.txt'
            content = text[len('write '):]
            self.write(filename, content)
