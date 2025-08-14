import time
import json
from services.base_service import BaseService
from services.config import config


class SystemInfoService(BaseService):
    def __init__(self, *queues):
        super().__init__()
        self.queues = list(queues)
        self.enabled_metrics = [m for m in config.METRICS if m.enabled]

    def run(self):
        while not self._stop_event.is_set():
            data = {"timestamp": time.time()}
            for metric in self.enabled_metrics:
                try:
                    data[metric.json_key] = metric.collector_function()
                except Exception as e:
                    print(f"Error collecting {metric.display_name}: {e}")
                    data[metric.json_key] = None

            for q in self.queues:
                q.put(json.dumps(data))
            time.sleep(config.CYCLE_DURATION)