import json

import speech_recognition as sr
from speech_recognition.exceptions import WaitTimeoutError
from assistant.settings.default_settings import settings
from assistant.manager import CommandManager

recognizer = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=3)
        except WaitTimeoutError:
            return None
    return audio

def recognize_speech(audio):
    if not audio:
        return None
    try:
        text = recognizer.recognize_vosk(audio, language=settings.input_language)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")


def get_voice_input():
    audio = record_audio()
    text = recognize_speech(audio)
    try:
        text = json.loads(text)
        text = text["text"]
    except:
        pass
    return text

