import json
import logging

from src.util.logger import setup
from src.manager import MonitorManagerBuilder, MonitorTypes
from src.components.receiver import UIReceiver


def _read_config(path):
    with open(path, 'r') as config_file:
        return json.load(config_file)


def _log_level(config):
    debug = config.get('debug', False)
    return logging.DEBUG if debug else logging.INFO


def _build_monitors(config):
    builder = MonitorManagerBuilder()

    for monitor, enabled in config.get('monitors', {}).items():
        if enabled and hasattr(MonitorTypes, monitor):
            builder.add_monitor(getattr(MonitorTypes, monitor))

    monitor_manager, shared_queue, monitor_count = builder.build()
    return monitor_manager, shared_queue, monitor_count


def main(config_path):
    try:
        config = _read_config(str(config_path))
    except FileNotFoundError:
        logging.error(f'Config file not found ({config_path})')
        return
    except json.decoder.JSONDecodeError:
        logging.error(f'Bad config file ({config_path})')
        return

    logger = setup(_log_level(config))
    
    monitor_manager, shared_queue, monitor_count = _build_monitors(config)
    if monitor_count == 0:
        logging.error('No monitors enabled')
        return

    ui = UIReceiver(shared_queue, monitor_count)
    try:
        monitor_manager.start()
        ui.start()  # blocking
        logger.info('Exiting...')
        monitor_manager.stop()

    except KeyboardInterrupt:
        logger.info('Exiting...')
        monitor_manager.stop()
