from dataclasses import dataclass, field
from typing import List
from utils.system_info_collectors_utils import (
    MetricCollector,
    CpuPercentCollector,
    RamPercentCollector,
    DiskPercentCollector,
    DiskUsedMBCollector,
    NetworkSentMBCollector, RamUsedGBCollector,
)

@dataclass
class Metric:
    display_name: str
    json_key: str
    unit: str
    collector: MetricCollector
    enabled: bool = True

@dataclass
class Config:
    CYCLE_DURATION: int = 1
    METRICS: List[Metric] = field(default_factory=lambda: [
        Metric(
            display_name="CPU Usage",
            json_key="cpu_percent",
            unit="%",
            collector=CpuPercentCollector(),
            enabled=True,
        ),
        Metric(
            display_name="Memory Usage",
            json_key="ram_percent",
            unit="%",
            collector=RamPercentCollector(),
            enabled=True,
        ),
        Metric(
            display_name="Memory Used",
            json_key="ram_used_gb",
            unit="GB",
            collector=RamUsedGBCollector(),
            enabled=True,
        ),
        Metric(
            display_name="Disk Usage",
            json_key="disk_percent",
            unit="%",
            collector=DiskPercentCollector(path="C:/"),
            enabled=True,
        ),
        Metric(
            display_name="Disk Used",
            json_key="disk_mb",
            unit="MB",
            collector=DiskUsedMBCollector(path="C:/"),
            enabled=False,
        ),
        Metric(
            display_name="Network Sent",
            json_key="network_sent",
            unit="MB",
            collector=NetworkSentMBCollector(),
            enabled=False,
        ),
    ])

config = Config()