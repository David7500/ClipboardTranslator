# Clipboard Translator

Clipboard Translator is a simple GUI application built using PyQt5 and Python that monitors your clipboard for changes. When you copy a word, it fetches its definition and translates it to a language of your choice. The translation and definitions are displayed in a window that can be resized automatically to fit the content.

## Features
- **Clipboard Monitoring**: Continuously checks the clipboard for changes.
- **Word Definition Fetching**: Retrieves the definition of a word from a dictionary API.
- **Translation**: Automatically translates the definition or copied text to a selected language using Google Translate.
- **Resizable Window**: The window adjusts its size based on the content, making it efficient for displaying long definitions or translations.
- **Language Selection**: Users can choose the language for translation from a predefined list, and the preference is saved for future use.
- **Esc Key Functionality**: Press the `Esc` key to hide the window.
- **Drag to Move**: The window can be moved around by dragging it with the mouse.

## Installation
git clone
source venv/bin/activate
python3 -m venv venv


Before running the program, you need to install the following Python dependencies:

- `PyQt5`: For the graphical user interface (GUI).
- `pynput`: To listen for keypress events (e.g., Esc key to hide the window).
- `requests`: For making HTTP requests to fetch word definitions.
- `deep_translator`: For translating text via Google Translate.

You can install the required dependencies using `pip`:

```bash
pip install PyQt5 pynput requests deep_translator
