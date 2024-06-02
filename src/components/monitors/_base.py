import time
import json


class BaseMonitor:
    """
    Base Monitor class monitors data at intervals
    Inherited by other classes for specific monitor unit
    """

    def __init__(self, name, get_info, shared_queue):
        self.name = name
        self.get_info = get_info
        self.shared_queue = shared_queue

        self._running = False
        self.interval = 1

    def monitor(self):
        self._running = True

        while self._running:
            start_time = time.time()

            data = self.get_info()
            if (not self.shared_queue.full()) and len(data) > 0:
                info = json.dumps({"unit": self.name, "data": data})
                self.shared_queue.put(info)

            elapsed_time = time.time() - start_time
            if elapsed_time < self.interval:
                time.sleep(self.interval - elapsed_time)

    def stop(self):
        self._running = False
