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

## Requirements

Before running the program, you need to install the following Python dependencies:

- `PyQt5`: For the graphical user interface (GUI).
- `pynput`: To listen for keypress events (e.g., Esc key to hide the window).
- `requests`: For making HTTP requests to fetch word definitions.
- `deep_translator`: For translating text via Google Translate.

## Setting up the Virtual Environment

To keep dependencies isolated and avoid conflicts with other Python projects, it's recommended to create a virtual environment for the project.

1. **Create a virtual environment**:

   Run the following command to create a virtual environment named `venv`:

   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment**:

   - On **Linux/macOS**, use:

     ```bash
     source venv/bin/activate
     ```

   - On **Windows**, use:

     ```bash
     .\venv\Scripts\activate
     ```

3. **Install dependencies**:

   Once the virtual environment is activated, install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. Clone the repository or download the script.
2. Ensure all required dependencies are installed (use `pip install -r requirements.txt` if the dependencies are listed in a `requirements.txt` file).
3. Run the program:

   ```bash
   python main.py
   ```

Once the application is running, the window will remain hidden by default. It will appear automatically when new text is copied to your clipboard.

## Usage

- **Clipboard Monitoring**: The program continuously monitors the clipboard for any changes. When a word is copied, it fetches its definition from a dictionary API and translates it into the selected language.

- **Language Selection**: You can select the target language for translation from the toolbar menu. The available languages are:
  - English (`en`)
  - Slovenian (`sl`)
  - French (`fr`)
  - German (`de`)
  - Spanish (`es`)

  The selected language is saved in the system settings and will persist across sessions.

- **Window Behavior**: You can drag the window by clicking and holding the left mouse button. The window will automatically resize based on the content, but you can manually resize it as well.

- **Hide Window**: Press the `Esc` key to hide the window when it's visible.

## Configuration

The application allows you to configure the following settings:

- **Window Width**: Set by `WINDOW_WIDTH`.
- **Font Size**: Set by `FONT_SIZE`.
- **Language**: Set by `TARGET_LANGUAGE`.

You can modify these values in the code to fit your preferences.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **PyQt5**: A set of Python bindings for Qt libraries for creating graphical user interfaces.
- **pynput**: A library used to monitor and control input devices.
- **requests**: A simple HTTP library for Python.
- **deep_translator**: A Python library that uses Google Translate API for translation.
- **Dictionary API**: The application fetches word definitions from the [Dictionary API](https://dictionaryapi.dev/).

