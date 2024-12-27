import uuid

from gtts import gTTS
import os
from assistant.settings.default_settings import settings
import playsound

class Speaker:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Speaker, cls).__new__(cls)
        return cls.instance

    def speak(self, text):
        print("Asking to speak: " + text)
        tts = gTTS(text, lang=settings.output_language)
        unique_id = str(uuid.uuid4())
        fullpath = settings.speaches_location / f"{unique_id}.mp3"
        tts.save(fullpath)
        playsound.playsound(fullpath, True)
        os.remove(fullpath)

