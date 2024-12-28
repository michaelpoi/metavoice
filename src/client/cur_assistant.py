from pathlib import Path
import sounddevice

from assistant.settings.default_settings import configure_settings, settings
from assistant.manager import CommandManager
from assistant.assistant import Assistant

configure_settings(debug=True,
                   input_language='ru',
                   output_language='ru',
                   modules=['greets', 'files'],
                   write_location=settings.BASE_DIR/'notes',
                   speaches_location=settings.BASE_DIR/'speaches',)
voice_assistant = Assistant()
voice_assistant.load_modules()
print(CommandManager.show())

