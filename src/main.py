import time
from src.manager import ManagerBuilder, Monitors

builder = ManagerBuilder()
manager = builder.add_monitor(Monitors.CPU_MONITOR).add_monitor(Monitors.MEM_MONITOR).build()

try:
    manager.start()
    time.sleep(5)
    manager.stop()
except KeyboardInterrupt:
    print("Exiting...")
    manager.stop()
