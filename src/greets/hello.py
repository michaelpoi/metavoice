import os

from assistant.command.icommand import ICommand
from assistant.storage import consistent_storage
from assistant.core.i18n import _

class HelloCommand(ICommand):
    find_patterns = {
        'en':['(hello|hi|hey)'],
        'ru':['(привет|здорово)']
    }
    def handle(self, text, **kwargs):
        if not consistent_storage.exists('name') or True:
            return self.respond(_("Hi sir"))
        else:
            return self.respond(f"Hi {consistent_storage.get('name')}")

class SetNameCommand(ICommand):
    find_patterns = ['my name is {name}', 'call me {name}', "называй меня {name}"]

    def handle(self, text, **kwargs):
       name = kwargs['name'].capitalize()
       consistent_storage.set('name', name)
       return self.respond(f"{_('Hello')} {name}!")

class GetNameCommand(ICommand):
    find_patterns = {
        'en':['who am I', 'what is my name'],
        'ru':['кто я', 'как меня зовут']
    }

    def handle(self, text, **kwargs):
        if not consistent_storage.exists('name'):
            return self.respond("Я не знаю вашего имени")
        else:
            name = consistent_storage.get('name')
            return self.respond(f'Ваше имя {name}')