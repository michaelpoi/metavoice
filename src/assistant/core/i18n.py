import gettext

from assistant.settings.default_settings import settings

def get_translation():
    locale_path = settings.BASE_DIR / 'merged_locale'
    print(locale_path)
    language = settings.output_language
    try:
        translation = gettext.translation('merged', locale_path, languages=[language], fallback=True)
    except FileNotFoundError:
        translation = gettext.NullTranslations()
    return translation.gettext

_ = get_translation()

