from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import json
import time


class MonitorUI(QtWidgets.QWidget):
    def __init__(self, queue, history_len=60):
        super().__init__()
        self.queue = queue
        self.history_len = history_len
        self.times, self.cpu, self.ram = [], [], []

        layout = QtWidgets.QVBoxLayout(self)
        self.plot_cpu = pg.PlotWidget(title="CPU Usage (%)")
        self.plot_ram = pg.PlotWidget(title="RAM Usage (%)")
        layout.addWidget(self.plot_cpu)
        layout.addWidget(self.plot_ram)

        self.curve_cpu = self.plot_cpu.plot(pen=pg.mkPen(width=2))
        self.curve_ram = self.plot_ram.plot(pen=pg.mkPen(width=2))
        self.plot_cpu.setYRange(0, 100)
        self.plot_ram.setYRange(0, 100)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)

    def _drain(self):
        got = False
        while not self.queue.empty():
            data = json.loads(self.queue.get())
            self.times.append(int(data["timestamp"]))
            self.cpu.append(data["cpu_percent"])
            self.ram.append(data["ram_percent"])
            got = True
        if len(self.times) > self.history_len:
            self.times = self.times[-self.history_len:]
            self.cpu = self.cpu[-self.history_len:]
            self.ram = self.ram[-self.history_len:]
        return got

    def update_plot(self):
        if self._drain():
            x0 = self.times[-1]
            xs = [t - (x0 - self.history_len) for t in self.times]
            self.curve_cpu.setData(xs, self.cpu)
            self.curve_ram.setData(xs, self.ram)
            if self.cpu:
                self.plot_cpu.setTitle(f"CPU Usage ({self.cpu[-1]:.1f}%)")
            if self.ram:
                self.plot_ram.setTitle(f"RAM Usage ({self.ram[-1]:.1f}%)")

    def run(self):
        self.setWindowTitle("System Monitor")
        self.resize(800, 1000)
        self.show()
