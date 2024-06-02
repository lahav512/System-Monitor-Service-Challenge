from src.components.monitors._base import BaseMonitor
from src.util.component_info import Components


class CPUMonitor(BaseMonitor):
    def __init__(self, shared_queue):
        super().__init__('CPU', Components.get_cpu, shared_queue)


class MEMMonitor(BaseMonitor):
    def __init__(self, shared_queue):
        super().__init__('Memory', Components.get_mem, shared_queue)


class RNDMonitor(BaseMonitor):
    def __init__(self, shared_queue):
        super().__init__('Random', Components.get_random, shared_queue)


class MonitorTypes:
    CPU_MONITOR = 1
    MEM_MONITOR = 2
    RND_MONITOR = 3

    @staticmethod
    def get_monitor_from_type(monitor):
        if monitor == MonitorTypes.CPU_MONITOR:
            return CPUMonitor
        elif monitor == MonitorTypes.MEM_MONITOR:
            return MEMMonitor
        elif monitor == MonitorTypes.RND_MONITOR:
            return RNDMonitor
