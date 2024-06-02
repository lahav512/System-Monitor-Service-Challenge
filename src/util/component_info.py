import psutil


class Components:

    @staticmethod
    def get_mem():
        try:
            memory_info = psutil.virtual_memory()

            return {
                'total': round(memory_info[0] / (1024 ** 3), 2),
                'available': round(memory_info[1] / (1024 ** 3), 2),
                'percent': memory_info[2],
                'used': round(memory_info[3] / (1024 ** 3), 2),
                'free': round(memory_info[4] / (1024 ** 3), 2)
            }
        except Exception:
            return {}
    
    @staticmethod
    def get_cpu():
        try:
            cpu_info = (psutil.cpu_percent(0.5),)

            return {
                'usage': cpu_info[0]
            }
        except Exception:
            return {}