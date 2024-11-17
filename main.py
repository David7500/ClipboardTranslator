import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QSizePolicy, QScrollArea, QMainWindow, QToolBar, QAction
from PyQt5.QtCore import QTimer, Qt, QPoint
from pynput import keyboard
import time
import requests
from deep_translator import GoogleTranslator

def fetch_definition(word):
    """
    Fetches the definition of the given word from the dictionary API.

    Args:
        word (str): The word for which to fetch the definition.

    Returns:
        str: HTML-formatted string containing the definitions or an error message.
    """
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    result = ""

    if response.status_code == 200:
        data = response.json()
        if 'meanings' in data[0]:
            for meaning in data[0]['meanings']:
                result += f"<b>{word.upper()}</b> - {meaning['partOfSpeech'].upper()}<br>"
                definition_counter = 1
                for definition in meaning['definitions']:
                    result += f"{definition_counter}. {definition['definition']}<br>"
                    definition_counter += 1
        else:
            result = "No definition found for this word.<br>"
    else:
        result = f"Error fetching definition. Status code: {response.status_code}<br>"

    return result

def fetch_translation(text, lang="sl"):
    """
    Translates the given text from English to the specified language using Google Translator.

    Args:
        text (str): The text to translate.
        lang (str): Target language code.

    Returns:
        str: The translated text.
    """
    translation = ""
    try:
        translation = GoogleTranslator(source='en', target=lang).translate(text)
    except:
        translation = "Text length needs to be between 0 and 5000 characters"
    return translation

class ClipboardMonitor(QMainWindow):
    """
    A GUI application that monitors the clipboard for changes, fetches
    word definitions and translations, and displays them.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clipboard Monitor")
        self.setGeometry(63, 0, 300, 870)
        # Remove the window frame
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Create the main label to display text
        self.text_label = QLabel("", self)
        self.text_label.setAlignment(Qt.AlignLeft)
        self.text_label.setWordWrap(True)
        font = self.text_label.font()
        font.setPointSize(FONT_SIZE)  # Set the font size to 14 points
        self.text_label.setFont(font)

        # Add a scrollable area for the label
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.text_label)
        self.scroll_area.setFixedWidth(WINDOW_WIDTH)

        # Set up the layout
        self.setCentralWidget(self.scroll_area)

        # Clipboard-related setup
        self.clipboard = QApplication.clipboard()
        self.previous_clipboard_text = ""
        self.clipboard_check_timer = QTimer(self)
        self.clipboard_check_timer.timeout.connect(self.check_clipboard)
        self.clipboard_check_timer.start(100)  # Check clipboard every 100ms

        self.hide()  # Start with the window hidden
        self.start_key_listener()

        # Initialize the mouse press position
        self.drag_position = None

    def adjust_window_size(self):
        """
        Adjust the window size based on the content of the displayed text.
        """
        self.setFixedHeight(1)
        self.adjustSize()
        content_height = self.text_label.size().height()
        if content_height >= MAX_HEIGHT:
            self.setFixedHeight(MAX_HEIGHT)
        else:
            self.setFixedHeight(content_height)

        # Refresh the window to reflect changes
        self.hide()
        self.show()

    def check_clipboard(self):
        """
        Checks if the clipboard content has changed. If it has, fetches the word
        definition and translation, and updates the display.
        """
        current_text = self.clipboard.text()
        if current_text != self.previous_clipboard_text:  # Clipboard content changed
            self.previous_clipboard_text = current_text
            start_time = time.time()
            if not " " in current_text:
                # Fetch definition and translation
                definition = fetch_definition(current_text)
                translation = fetch_translation(definition, TARGET_LANGUAGE)
                display_text = definition + "<p style='color: rgb(0, 0, 255);'>" + translation + "</p>"
            else:
                translation = fetch_translation(current_text, TARGET_LANGUAGE)
                display_text = "<p style='color: rgb(0, 0, 255);'>" + translation + "</p>"
            print(current_text + "   " + str(time.time() - start_time))

            # Combine and display results
            self.text_label.setText(display_text)
            self.scroll_area.verticalScrollBar().setValue(0)
            self.adjust_window_size()

    def start_key_listener(self):
        """
        Starts a key listener to monitor for specific key presses (e.g., Esc to hide the window).
        """
        def on_press(key):
            try:
                if key == keyboard.Key.esc:  # Detect the Esc key
                    self.hide()
            except Exception as e:
                print(f"Error: {e}")

        listener = keyboard.Listener(on_press=on_press)
        listener.start()

    def mousePressEvent(self, event):
        """
        Initiates the dragging of the window.
        """
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        """
        Moves the window according to the mouse movement.
        """
        if self.drag_position:
            self.move(event.globalPos() - self.drag_position)

    def mouseReleaseEvent(self, event):
        """
        Resets the drag position.
        """
        self.drag_position = None


if __name__ == "__main__":
    # Main application entry point
    app = QApplication(sys.argv)
    MAX_HEIGHT = app.primaryScreen().availableGeometry().height()
    WINDOW_WIDTH = 300
    TARGET_LANGUAGE = "sl"  # Language code for translation
    FONT_SIZE = 11
    monitor = ClipboardMonitor()
    sys.exit(app.exec_())
