import time
import json


class Receiver:
    """
    Receiver class fetches data from shared queue and passes to output
    """
    def __init__(self, shared_queue, monitor_count):
        self.shared_queue = shared_queue
        self.monitor_count = monitor_count
        self._running = False
        self.interval = 1
    
    def start(self):
        self._running = True

        while self._running:
            start_time = time.time()

            print("RECEIVER: queue length", self.shared_queue.qsize())
            if self.shared_queue.full():
                print("RECEIVER: queue empty")
            else:
                if self.shared_queue.qsize() >= self.monitor_count:
                    for _ in range(self.monitor_count):
                        data = json.loads(self.shared_queue.get())
                        print(data)

            elapsed_time = time.time() - start_time
            if elapsed_time < self.interval:
                time.sleep(self.interval - elapsed_time)
    
    def stop(self):
        self._running = False
