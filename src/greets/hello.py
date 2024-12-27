from assistant.command.icommand import ICommand
from assistant.storage import consistent_storage
from gettext import gettext as _


class HelloCommand(ICommand):
    find_patterns = ['hello', 'привет', "ассистент"]
    def handle(self, text):
        if not consistent_storage.exists('name'):
            return self.respond("Hi sir")
        else:
            return self.respond(f"Hi {consistent_storage.get('name')}")

class SetNameCommand(ICommand):
    find_patterns = ['my name is', 'call me', "называй меня"]

    def handle(self, text):
       name = text.split(' ')[-1].capitalize()
       consistent_storage.set('name', name)
       return self.respond(f"{_('Hello')} {name}!")

class GetNameCommand(ICommand):
    find_patterns = ['кто я', 'как меня зовут']

    def handle(self, text):
        if not consistent_storage.exists('name'):
            return self.respond("Я не знаю вашего имени")
        else:
            name = consistent_storage.get('name')
            return self.respond(f'Ваше имя {name}')