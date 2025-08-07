import time
import json
import psutil
from services.base_service import BaseService
from services.config import Config


class SystemInfoService(BaseService):
    def __init__(self, *queues):
        super().__init__()
        self.queue = list(queues)

    def run(self):
        while not self._stop_event.is_set():
            data = {
                "timestamp": time.time(),
                "cpu_percent": psutil.cpu_percent(),
                "ram_percent": psutil.virtual_memory().percent,
            }
            for q in self.queue:
                q.put(json.dumps(data))
            time.sleep(Config.CYCLE_DURATION)
