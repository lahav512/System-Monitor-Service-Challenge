
import threading
import queue

from src.components.monitors.units import Monitors
from src.components.receiver import Receiver


class _Manager:
    """
    Manager class responsible for initializing, starting & stopping receiver and montior threads
    """
    def __init__(self):
        self.monitors = []
        self.receiver = None
        self.shared_queue = None

        self.monitor_threads = []
        self.receiver_thread = None

        self._running = False
        self._initialized = False

    def add_monitor(self, monitor):
        self.monitors.append(monitor)

    def monitor_count(self):
        return len(self.monitors)
    
    def initialize(self):
        self.shared_queue = queue.Queue(maxsize=len(self.monitors)*3)
        self.receiver = Receiver(self.shared_queue, len(self.monitors))
        self.monitors = [m(self.shared_queue) for m in self.monitors]

        print(self.monitors)
        print(self.receiver)

        self._initialized = True
    
    def initialize_threads(self):
        self.monitor_threads.clear()
        for monitor in self.monitors:
            self.monitor_threads.append(threading.Thread(target=monitor.monitor))
        self.receiver_thread = threading.Thread(target=self.receiver.start)
    
    def start(self):
        if not self._running and self._initialized:
            self.initialize_threads()
            self._running = True

            for mt in self.monitor_threads:
                mt.start()
            self.receiver_thread.start()
      
    def stop(self):
        for m in self.monitors:
            m.stop()
        self.receiver.stop()

        for mt in self.monitor_threads:
            mt.join()
        self.receiver_thread.join()

        self._running = False


class ManagerBuilder:
    def __init__(self):
        self.manager = _Manager()

    def add_monitor(self, monitor):
        monitor_unit = Monitors.get_monitor_unit(monitor)
        if monitor_unit:
            self.manager.add_monitor(monitor_unit)
        return self

    def build(self):
        self.manager.initialize()
        return self.manager
