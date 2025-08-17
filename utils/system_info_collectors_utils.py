from abc import ABC, abstractmethod
import psutil

class MetricCollector(ABC):
    @abstractmethod
    def collect(self):
        pass

class CpuPercentCollector(MetricCollector):
    def collect(self):
        return psutil.cpu_percent()

class RamPercentCollector(MetricCollector):
    def collect(self):
        return psutil.virtual_memory().percent

class RamUsedGBCollector(MetricCollector):
    def collect(self):
        return psutil.virtual_memory().used / (1024 ** 3)

class DiskPercentCollector(MetricCollector):
    def __init__(self, path: str = "C:/"):
        self.path = path
    def collect(self):
        return psutil.disk_usage(self.path).percent

class DiskUsedMBCollector(MetricCollector):
    def __init__(self, path: str = "C:/"):
        self.path = path
    def collect(self):
        return psutil.disk_usage(self.path).used / (1024 * 1024)

class NetworkSentMBCollector(MetricCollector):
    def collect(self):
        return psutil.net_io_counters().bytes_sent / (1024 * 1024)
