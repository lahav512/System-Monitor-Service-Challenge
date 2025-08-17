from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import json
from services.config import config


class MonitorUI(QtWidgets.QWidget):
    def __init__(self, queue, history_len=60):
        super().__init__()
        self.queue = queue
        self.history_len = history_len

        self.times = []
        self.metrics = {m.display_name: [] for m in config.METRICS if m.enabled}
        self.metric_configs = {m.display_name: m for m in config.METRICS if m.enabled}

        self.curves = {}
        self.plots = {}

        layout = QtWidgets.QVBoxLayout(self)

        # Create one plot per enabled metric from the config
        for name in self.metrics:
            plot = pg.PlotWidget(title=f"{name} ({self.metric_configs[name].unit})")
            plot.setYRange(0, 100)
            layout.addWidget(plot)
            self.plots[name] = plot
            self.curves[name] = plot.plot(pen=pg.mkPen(width=2))

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)

    def _drain(self):
        got = False
        while not self.queue.empty():
            data = json.loads(self.queue.get())
            self.times.append(data["timestamp"])

            for display_name, metric_config in self.metric_configs.items():
                key = metric_config.json_key
                self.metrics[display_name].append(data.get(key, 0))

            got = True

        if len(self.times) > self.history_len:
            self.times = self.times[-self.history_len:]
            for k in self.metrics:
                self.metrics[k] = self.metrics[k][-self.history_len:]

        return got

    # Update all graphs with latest data from the queue
    def update_plot(self):
        if self._drain():
            x0 = self.times[-1]
            xs = [t - (x0 - self.history_len) for t in self.times]

            for display_name, curve in self.curves.items():
                unit = self.metric_configs[display_name].unit
                current_value = self.metrics[display_name][-1]
                curve.setData(xs, self.metrics[display_name])
                if unit == "%":
                    self.plots[display_name].setTitle(f"{display_name} ({current_value:.1f}%)")
                else:
                    self.plots[display_name].setTitle(f"{display_name} ({current_value:.1f} {unit})")

    # Show the UI with size based on number of enabled metrics
    def run(self):
        self.setWindowTitle("System Monitor")
        self.resize(800, 300 * max(1, len(self.metrics)))
        self.show()