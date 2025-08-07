import platform
import sys
from queue import Queue
from PyQt5 import QtWidgets

from services.system_info_service import SystemInfoService
from services.system_info_presentor_service import SystemInfoPresentorService
from ui.monitor_ui import MonitorUI

if __name__ == "__main__":
    if platform.system() != "Windows":
        print("This system monitor currently supports only Windows OS.")
        sys.exit(1)
    q = Queue()
    z = Queue()
    sysinfo = SystemInfoService(q, z)
    sysinfo_presentor = SystemInfoPresentorService(queue=z)
    sysinfo.start()
    sysinfo_presentor.start()


    app = QtWidgets.QApplication(sys.argv)
    ui = MonitorUI(q)
    try:
        ui.run()
        exit_code = app.exec_()
    finally:
        sysinfo_presentor.stop()
        sysinfo.stop()
    sys.exit(exit_code)