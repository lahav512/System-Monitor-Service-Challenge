# System Monitor

System resource monitor viewer

## Usage

First install the required libraries:

```
pip install -r requirements.txt
```

Then to run the system monitor:

```
python monitor.py
```

You can also modify data shown with the `config.json` file:

```json
{
  "monitors": {
    "CPU_MONITOR": true,
    "MEM_MONITOR": true,
    "RND_MONITOR": false
  },
  "debug": true
}
```

## For Devs

To add new monitors modify these files:

#### `src/util/component_info.py`

Add a static method to the `Components` class with your data retrieval method of choice:

```python
@staticmethod
def get_example():
    try:
        example_info = example_get_data()

        return {
            'usage': example_info[0],  # data (%) shown on graph
            'info': {  # data shown as labels
                'Data 1': example_info[1]
                'Data 2': example_info[2]
            }
        }
    except Exception as e:
        logger.exception(e)
        return {}
```

#### `src/components/monitors/units.py`

Add your monitor as a class:

```python
class CPUMonitor(BaseMonitor):
    def __init__(self, shared_queue):
        super().__init__('CPU', Components.get_cpu, shared_queue)
...

# Here
class EXAMPLEMonitor(BaseMonitor):
    def __init__(self, shared_queue):
        super().__init__('Example', Components.get_example, shared_queue)


class MonitorTypes:
    CPU_MONITOR = 1
    ...
    # Here
    EXAMPLE_MONITOR = 4

    @staticmethod
    def get_monitor_from_type(monitor):
        if monitor == MonitorTypes.CPU_MONITOR:
            return CPUMonitor
        ...
        # Here
        elif monitor == MonitorTypes.EXAMPLE_MONITOR:
            return EXAMPLEMonitor
```

#### `config.json`

Add your new monitor to the config and you're done.

```json
"monitors": {
  "CPU_MONITOR": true,
  ...
  "EXAMPLE_MONITOR": true
}
```
