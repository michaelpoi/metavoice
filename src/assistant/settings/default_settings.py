from pathlib import Path

from assistant.storages.istorage import IStorage


class AssistantSettings:
    def __init__(self):
        self.modules = ['greets']
        self.debug = False
        self.BASE_DIR = Path(__file__).resolve().parent.parent.parent
        self.use_i18n = True

    def set_setting(self, key, value):
        if key == 'temp_storage' or key == 'consistent_storage':
            if not issubclass(value, IStorage):
                raise ValueError('Storage must be a subclass of IStorage')

        setattr(self, key, value)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

def configure_settings(**kwargs):
    settings.update(**kwargs)


settings = AssistantSettings()
