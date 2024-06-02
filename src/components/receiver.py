import numpy as np
import matplotlib.pyplot as plt
import time
import json


class UIReceiver:
    """
    UI Receiver class fetches data from shared queue and outputs with matplotlib
    """

    def __init__(self, shared_queue, monitor_count):
        self.shared_queue = shared_queue
        self.monitor_count = monitor_count
        self._running = False
        self.interval = 1

        self.fig = None
        self.axes = None
        self.axes_counter = 0
        self.plots = {}

    def initialize_ui(self):
        self.fig, self.axes = plt.subplots(1, self.monitor_count, figsize=(5 * self.monitor_count, 5))
        self.fig.canvas.mpl_connect('close_event', self.stop)

        if type(self.axes) != np.ndarray:  # monitor_count is 1
            self.axes = np.array([self.axes])

    def update_or_create_plot(self, data):
        try:
            # Plot exists
            self.plots[data['unit']]['data'] = data['data']

        except KeyError:
            # Plot doesn't exist, initialize
            self.axes[self.axes_counter].set_xlim(0, 20)
            self.axes[self.axes_counter].set_ylim(0, 100)
            self.axes[self.axes_counter].set_title(f"{data['unit']} Monitor")
            self.axes[self.axes_counter].set_xlabel('Time (s)')
            self.axes[self.axes_counter].set_ylabel('Usage (%)')
            self.axes[self.axes_counter].invert_xaxis()
            text = self.axes[self.axes_counter].text(10, 90, '', ha='center', va="top")
            line, = self.axes[self.axes_counter].plot([], [])
            self.plots[data['unit']] = {
                'data': data['data'],
                'line': line,
                'text': text,
                'x_list': np.linspace(0, 20, num=20),
                'y_list': np.zeros(20),

            }

            self.axes_counter += 1

    def update_plot_ui(self, unit):
        self.plots[unit]['y_list'][1:] = self.plots[unit]['y_list'][:-1]
        self.plots[unit]['y_list'][0] = self.plots[unit]['data']['usage']

        self.plots[unit]['line'].set_data(self.plots[unit]['x_list'], self.plots[unit]['y_list'])
        self.plots[unit]['text'].set_text(
            "\n".join(f"{key}: {value}" for key, value in self.plots[unit]['data']['info'].items()))

    def start(self):
        self.initialize_ui()
        self._running = True

        while self._running:
            start_time = time.time()

            print("RECEIVER: queue length", self.shared_queue.qsize())

            for _ in range(self.shared_queue.qsize()):
                data = json.loads(self.shared_queue.get())
                print(data)
                self.update_or_create_plot(data)
                self.update_plot_ui(data['unit'])

            elapsed_time = time.time() - start_time
            if elapsed_time < self.interval:
                plt.pause(self.interval - elapsed_time)

        plt.close()

    def stop(self, event=None):
        self._running = False
