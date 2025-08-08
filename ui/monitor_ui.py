from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import json
from services.config import Config


class MonitorUI(QtWidgets.QWidget):
    def __init__(self, queue, history_len=60):
        super().__init__()
        self.queue = queue
        self.history_len = history_len

        self.times = []
        self.metrics = {name: [] for name in self._enabled_metrics()}
        self.curves = {}
        self.plots = {}

        layout = QtWidgets.QVBoxLayout(self)

        # Create one plot per enabled metric
        for name in self.metrics:
            plot = pg.PlotWidget(title=name)
            plot.setYRange(0, 100)
            layout.addWidget(plot)
            self.plots[name] = plot
            self.curves[name] = plot.plot(pen=pg.mkPen(width=2))
        #Update graphs every second
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)

    def _enabled_metrics(self):
        mapping = {
            "CPU Usage (%)": Config.SHOW_CPU,
            "Memory Usage (%)": Config.SHOW_RAM,
            "Disk Usage (%)": Config.SHOW_DISK,
        }
        return [name for name, enabled in mapping.items() if enabled]

    #Pull all queued data points into self.metrics and self.times
    def _drain(self):
        got = False
        while not self.queue.empty():
            data = json.loads(self.queue.get())
            self.times.append(int(data["timestamp"]))

            # Map plot titles to json keys
            key_map = {
                "CPU Usage (%)": "cpu_percent",
                "Memory Usage (%)": "ram_percent",
                "Disk Usage (%)": "disk_percent",
            }
            for title in self.metrics:
                key = key_map[title]
                self.metrics[title].append(data.get(key, 0))

            got = True

        # Keep fixed history length
        if len(self.times) > self.history_len:
            self.times = self.times[-self.history_len:]
            for k in self.metrics:
                self.metrics[k] = self.metrics[k][-self.history_len:]

        return got

    #Update all graphs with latest data from the queue
    def update_plot(self):
        if self._drain():
            x0 = self.times[-1]
            xs = [t - (x0 - self.history_len) for t in self.times]
            for title, curve in self.curves.items():
                curve.setData(xs, self.metrics[title])
                if self.metrics[title]:
                    self.plots[title].setTitle(f"{title[:-3]} ({self.metrics[title][-1]:.1f}%)")

    # Show the UI with size based on number of enabled metrics
    def run(self):
        self.setWindowTitle("System Monitor")
        self.resize(800, 300 * max(1, len(self.metrics)))
        self.show()
