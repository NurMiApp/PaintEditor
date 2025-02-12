import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    DIRECTORY_TO_WATCH = "./"  # Set the path to the directory to watch

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'modified':
            # Take any action here when a file is modified.
            if event.src_path.endswith(".cpp"):
                print(f"Detected a change in {event.src_path}")
                # Here, you can place your code to trigger any action
                # For example, opening a file or running a command

if __name__ == '__main__':
    w = Watcher()
    w.run()
