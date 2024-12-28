import sys
import os
import glob
import subprocess
from pathlib import Path


def set_utf8(po_file):
    with open(po_file, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(po_file, 'w', encoding='utf-8') as f:
        f.write(content.replace('charset=ASCII', 'charset=UTF-8'))


def make_messages(package_name, language):
    locale_dir = os.path.join(package_name, 'locale')
    pot_file = os.path.join(locale_dir, f'{package_name}.pot')
    po_file = os.path.join(locale_dir, language, 'LC_MESSAGES', f'{package_name}.po')

    os.makedirs(os.path.dirname(po_file), exist_ok=True)
    python_files = glob.glob(os.path.join(package_name, '*.py'))

    if not python_files:
        raise FileNotFoundError(f"No Python files found in {package_name}")

    try:
        # Extract translatable strings from Python files using xgettext
        print(f"Extracting messages from {package_name} to {pot_file}...")
        subprocess.run(['xgettext', '--language=Python', '--keyword=_', '--output', pot_file] + python_files,
                       check=True)

        # Initialize the .po file for the specified language
        print(f"Initializing translation for language {language}...")
        subprocess.run(['msginit', '--locale', language, '--input', pot_file, '--output', po_file,
                        '--no-translator'], check=True)

        set_utf8(po_file)

        print(f"Translation file {po_file} initialized.")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running a command: {e}")
        print(f"Error details: {e.stderr}")

def merge_translations(package_names, language):
    BASE_DIR = Path(__file__).resolve().parent.parent
    locale_dir = BASE_DIR / 'merged_locale' / language / "LC_MESSAGES"
    merged_po = locale_dir / "merged.po"
    merged_mo = locale_dir / "merged.mo"

    os.makedirs(locale_dir, exist_ok=True)

    po_files = [
        BASE_DIR /  package/ "locale" / language / "LC_MESSAGES" / f"{package}.po"
        for package in package_names
    ]
    real_files = []
    for file in po_files:
        if not file.exists():
            print(f'Warning po file does not exist:{file}')
        else:
            real_files.append(file)

    try:
        # Merge .po files into a single .po file
        print(f"Merging translations for {language} into {merged_po}...")
        subprocess.run(['msgcat', '--use-first'] + real_files + ['-o', merged_po], check=True)

        set_utf8(merged_po)

        # Compile the merged .po file into a single .mo file
        print(f"Compiling merged translations into {merged_mo}...")
        subprocess.run(['msgfmt', merged_po, '-o', merged_mo], check=True)

        print(f"Merged translations successfully created at {merged_mo}.")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while merging or compiling translations: {e}")


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python translate.py <command> <package_name> <language>")
        sys.exit(1)

    command = sys.argv[1]
    language = sys.argv[2]
    package_name = sys.argv[3]
    additional_packages = sys.argv[4:]

    if command == 'makemessages':
        make_messages(package_name, language)
    elif command == 'merge':
        package_names = [package_name] + additional_packages
        merge_translations(package_names, language)