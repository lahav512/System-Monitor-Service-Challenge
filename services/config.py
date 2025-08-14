from dataclasses import dataclass, field
import psutil


def get_cpu_percent():
    return psutil.cpu_percent()


def get_ram_percent():
    return psutil.virtual_memory().percent


def get_disk_percent():
    return psutil.disk_usage('C:/').percent


def get_disk_mb():
    return psutil.disk_usage('C:/').used / (1024 * 1024)


def get_network_sent():
    return psutil.net_io_counters().bytes_sent / (1024 * 1024)


@dataclass
class Metric:
    display_name: str
    json_key: str
    unit: str
    collector_function: callable
    enabled: bool = True


@dataclass
class Config:
    CYCLE_DURATION: int = 1

    METRICS: list[Metric] = field(default_factory=lambda: [
        Metric(
            display_name="CPU Usage",
            json_key="cpu_percent",
            unit="%",
            collector_function=get_cpu_percent,
            enabled=True,
        ),
        Metric(
            display_name="Memory Usage",
            json_key="ram_percent",
            unit="%",
            collector_function=get_ram_percent,
            enabled=True,
        ),
        Metric(
            display_name="Disk Usage",
            json_key="disk_percent",
            unit="%",
            collector_function=get_disk_percent,
            enabled=False,
        ),
        Metric(
            display_name="Network Sent",
            json_key="network_sent",
            unit="MB",
            collector_function=get_network_sent,
            enabled=True,
        ),
        Metric(
            display_name="Disk Used",
            json_key="disk_mb",
            unit="MB",
            collector_function=get_disk_mb,
            enabled=False,
        )
    ])

config = Config()