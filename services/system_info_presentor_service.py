import json
import time
from services.base_service import BaseService
from services.config import Config


class SystemInfoPresentorService(BaseService):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while not self._stop_event.is_set():
            try:
                data_json = self.queue.get(timeout=1)
                data = json.loads(data_json)
                print(f"Timestamp: {data['timestamp']}, CPU: {data['cpu_percent']}%, RAM: {data['ram_percent']}%")
                time.sleep(Config.CYCLE_DURATION)
            except Exception as e:
                continue
