from ._base import BaseMonitor
from src.util.component_info import Components

class CPUMonitor(BaseMonitor):
    def __init__(self, shared_queue):
        super().__init__('cpu', Components.get_cpu, shared_queue)


class MEMMonitor(BaseMonitor):
    def __init__(self, shared_queue):
        super().__init__('mem', Components.get_mem, shared_queue)


class Monitors:
    CPU_MONITOR = 1
    MEM_MONITOR = 2

    @staticmethod
    def get_monitor_unit(monitor):
        if monitor == Monitors.CPU_MONITOR:
            return CPUMonitor
        elif monitor == Monitors.MEM_MONITOR:
            return MEMMonitor
