
from assistant import Assistant, configure_settings
from pathlib import Path
import sounddevice
if __name__ == '__main__':
    BASE_DIR = Path(__file__).resolve().parent.parent
    configure_settings(debug=False,
                       input_language='ru-Ru',
                       output_language='ru',
                       modules=['greets', 'files'],
                       write_location=BASE_DIR/'notes',
                       speaches_location=BASE_DIR/'speaches',)
    assistant = Assistant()
    print(assistant.process_command('hello'))
    assistant.serve()