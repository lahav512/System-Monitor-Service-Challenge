import threading
from abc import ABC, abstractmethod

class BaseService(ABC):
    def __init__(self):
        self._stop_event = threading.Event()
        self._thread = None

    def start(self):
        if self._thread is None:
            self._thread = threading.Thread(target=self.run, daemon=True)
            self._thread.start()

    def stop(self):
        self._stop_event.set()
        if self._thread is not None:
            self._thread.join()

    @abstractmethod
    def run(self):
        pass
