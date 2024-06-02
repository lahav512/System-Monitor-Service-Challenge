from src.manager import MonitorManagerBuilder, Monitors
from src.components.receiver import UIReceiver

builder = MonitorManagerBuilder()
monitor_manager, shared_queue, monitor_count = builder.add_monitor(
    Monitors.CPU_MONITOR).add_monitor(
    Monitors.MEM_MONITOR).build()
ui = UIReceiver(shared_queue, monitor_count)

try:
    monitor_manager.start()
    ui.start()  # blocking
    print("Exiting...")
    monitor_manager.stop()

except KeyboardInterrupt:
    print("Exiting...")
    monitor_manager.stop()
