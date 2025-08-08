from dataclasses import dataclass

@dataclass
class Config:
    CYCLE_DURATION: int = 1
    SHOW_CPU: bool = True
    SHOW_RAM: bool = True
    SHOW_DISK: bool = False
