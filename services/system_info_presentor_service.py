import json
import time
from services.base_service import BaseService
from services.config import config
from utils.presentor_utils import format_system_info

class SystemInfoPresentorService(BaseService):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while not self._stop_event.is_set():
            try:
                data_json = self.queue.get(timeout=1)
                data = json.loads(data_json)
                output = format_system_info(data)
                print(output)
                time.sleep(config.CYCLE_DURATION)
            except Exception:
                continue