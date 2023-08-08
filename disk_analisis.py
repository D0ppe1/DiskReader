import psutil
from psutil._common import bytes2human


def disk_analisis(disk: str):
    # Function that return information about a disk that user indicate
    total, used, free, percent = psutil.disk_usage(f'{disk}:/')
    # I guess that "total,used,free,percent" are parametrs of psutil.disk_usage
    # which help to get info about a disk
    for info in disk:
        print(
            f"Всего -- {bytes2human(total)} -- места на диске\n"
            f"Использованно -- {bytes2human(used)} -- места на диске\n"
            f"Свободно -- {bytes2human(free)} -- места на диске\n"
            f"Процент заполнения диска -- {percent}% --\n"
        )

    return info


print(disk_analisis("d"))  # In parantheses indicated a name of disk

