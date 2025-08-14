import json
import time
from services.base_service import BaseService
from services.config import config


class SystemInfoPresentorService(BaseService):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while not self._stop_event.is_set():
            try:
                data_json = self.queue.get(timeout=1)
                data = json.loads(data_json)

                parts = [f"Timestamp: {data.get('timestamp', 0)}"]
                if 'cpu_percent' in data:
                    parts.append(f"CPU: {data['cpu_percent']}%")
                if 'ram_percent' in data:
                    parts.append(f"RAM: {data['ram_percent']}%")
                if 'disk_percent' in data:
                    parts.append(f"Disk: {data['disk_percent']}%")

                print(", ".join(parts))
                time.sleep(config.CYCLE_DURATION)
            except Exception:
                continue