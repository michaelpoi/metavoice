from pathlib import Path
import sounddevice

from assistant.settings.default_settings import configure_settings
from assistant.manager import CommandManager
from assistant.assistant import Assistant

BASE_DIR = Path(__file__).resolve().parent.parent
configure_settings(debug=True,
                   input_language='ru-Ru',
                   output_language='ru',
                   modules=['greets', 'files'],
                   write_location=BASE_DIR/'notes',
                   speaches_location=BASE_DIR/'speaches',)
voice_assistant = Assistant()
voice_assistant.load_modules()
print(CommandManager.show())

