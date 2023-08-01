# import os
# import sys

import psutil

# В ф-ции нужно, чтобы мы определили:
# 1. Кол-во кортежей done
# 2. Нужно создать кол-во переменных равное кол-ву кортежей
# 3. Сделать из переменных список
# 4. Вывести нулевой индекс каждого списка


# function retrun a list of disks
def disk_list():
    # а - список с кортежами
    a = psutil.disk_partitions(all=False)
    lengtha = len(a)
    print(lengtha)

    print(a[0])
    # b - переменная которая берет 1-й кортеж
    b = a[0]
    # print(b)
    # превращаем b в список b
    b = list(b)
    # print(b)
    # возвращаем 0-вой индекс списка b
    return b[0]

print(disk_list())



# def disk_list():
    # templ = "%-17s"
    # print(templ % ('Disks:'))
    # for part in psutil.disk_partitions(all=False):
    #     if os.name == "nt":
    #         if 'cdrom' in part.opts or part.fstype == '':
    #             continue
    #     print(templ % (part.device))


# if __name__ == '__disk_list__':
#     sys.exit(disk_list())



# a = psutil.disk_partitions()
# print(a)
