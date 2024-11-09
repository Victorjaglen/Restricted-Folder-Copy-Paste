import pyperclip
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

ROOT_DIRECTORY = 'C:/restricted_root'  # Your root folder path


class ClipboardMonitor:
    def __init__(self, root_folder):
        self.root_folder = root_folder

    def check_clipboard(self):
        clipboard_content = pyperclip.paste()
        if self.is_restricted_content(clipboard_content):
            print("Blocked clipboard content from restricted folder.")
            pyperclip.copy('')

    def is_restricted_content(self, content):
        # Checking if the clipboard content is a path inside the root directory
        return content.startswith(self.root_folder)


class RestrictFolderHandler(FileSystemEventHandler):
    def __init__(self, root_folder):
        self.root_folder = root_folder
        self.clipboard_monitor = ClipboardMonitor(root_folder)

    def on_modified(self, event):
        # Trigger clipboard checking when any modification is detected
        self.clipboard_monitor.check_clipboard()


def monitor_root_folder(root_folder):
    event_handler = RestrictFolderHandler(root_folder)
    observer = Observer()
    observer.schedule(event_handler, path=root_folder, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    print(f"Monitoring {ROOT_DIRECTORY} for restricted copy-paste actions.")
    monitor_root_folder(ROOT_DIRECTORY)
