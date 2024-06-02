
import threading
import queue

from src.components.monitors.units import MonitorTypes


class _MonitorManager:
    """
    Manager class responsible for initializing, starting & stopping and monitor threads
    """
    def __init__(self):
        self.monitors = []
        self.monitor_threads = []
        self.shared_queue = None

        self._running = False
        self._initialized = False

    def add_monitor(self, monitor):
        self.monitors.append(monitor)

    def monitor_count(self):
        return len(self.monitors)
    
    def initialize(self):
        self.shared_queue = queue.Queue(maxsize=len(self.monitors))
        self.monitors = [m(self.shared_queue) for m in self.monitors]

        self._initialized = True
    
    def initialize_threads(self):
        self.monitor_threads.clear()
        for monitor in self.monitors:
            self.monitor_threads.append(threading.Thread(target=monitor.monitor))
    
    def start(self):
        if not self._running and self._initialized:
            self.initialize_threads()
            self._running = True

            for mt in self.monitor_threads:
                mt.start()
      
    def stop(self):
        for m in self.monitors:
            m.stop()

        for mt in self.monitor_threads:
            mt.join()

        self._running = False


class MonitorManagerBuilder:
    def __init__(self):
        self.manager = _MonitorManager()

    def add_monitor(self, monitor_type):
        monitor = MonitorTypes.get_monitor_from_type(monitor_type)
        if monitor:
            self.manager.add_monitor(monitor)
        return self

    def build(self):
        self.manager.initialize()
        return self.manager, self.manager.shared_queue, self.manager.monitor_count()
