import signal
from src import main

signal.signal(signal.SIGINT, lambda signum, frame: None)  # Disables KeyboardInterrupt signal
main.main(config_path='config.json')
