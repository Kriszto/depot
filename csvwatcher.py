import logging
import time
from typing import Callable

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class CsvWatcher:
    def __init__(self, directory: str, func: Callable):
        self.observer = Observer()
        self.directory = directory
        self.func = func
        self.running = False
        self.canRun = True

    def run(self):
        logging.info(f'watching {self.directory} directory')
        event_handler = Handler(self.func)
        self.observer.schedule(event_handler, self.directory, recursive=False)
        self.observer.start()
        self.running = True
        try:
            while self.canRun:
                time.sleep(5)
        except:
            self.observer.stop()
            logging.error("Error during loop")
            self.running = False
            self.observer.join()


class Handler(FileSystemEventHandler):
    def __init__(self, func):
        self.func = func

    def on_created(self, event):
        logging.info(f'got an event: {event.src_path}')
        if event.is_directory:
            return None
        if event.src_path.endswith('.csv'):
            self.func(event)
