import psutil
from psutil._common import bytes2human


def disk_analisis(disk: str):
    # Function that return information about a disk that user indicate
    total, used, free, percent = psutil.disk_usage(f'{disk}:/')
    # I guess that "total,used,free,percent" are parametrs of psutil.disk_usage
    # which help to get info about a disk

    stats = f"Всего -- {bytes2human(total)} -- места на диске "\
            f"Использованно -- {bytes2human(used)} -- места на диске "\
            f"Свободно -- {bytes2human(free)} -- места на диске "\
            f"Процент заполнения диска -- {int(percent)}% -- "\

    return stats

print(disk_analisis("c"))  # In parantheses indicated a name of disk
