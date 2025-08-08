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
            data = {"timestamp": time.time()}

            if Config.SHOW_CPU:
                data["cpu_percent"] = psutil.cpu_percent()
            if Config.SHOW_RAM:
                data["ram_percent"] = psutil.virtual_memory().percent
            if Config.SHOW_DISK:
                data["disk_percent"] = psutil.disk_usage('C:/').percent
            for q in self.queue:
                q.put(json.dumps(data))
            time.sleep(Config.CYCLE_DURATION)
