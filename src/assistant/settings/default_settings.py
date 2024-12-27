class AssistantSettings:
    def __init__(self):
        self.modules = ['greets']
        self.debug = False

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

def configure_settings(**kwargs):
    settings.update(**kwargs)


settings = AssistantSettings()
