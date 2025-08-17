def format_timestamp(data: dict) -> str:
    return f"Timestamp: {data.get('timestamp', 0)}"

def format_cpu(data: dict) -> str | None:
    if 'cpu_percent' in data:
        return f"CPU: {data['cpu_percent']}%"
    return None

def format_ram(data: dict) -> str | None:
    if 'ram_percent' in data:
        return f"RAM: {data['ram_percent']}%"
    return None

def format_disk(data: dict) -> str | None:
    if 'disk_percent' in data:
        return f"Disk: {data['disk_percent']}%"
    return None

def format_system_info(data: dict) -> str | None:
    parts = [format_timestamp(data)]
    for formatter in (format_cpu, format_ram, format_disk):
        formatted = formatter(data)
        if formatted:
            parts.append(formatted)
    return ", ".join(parts)