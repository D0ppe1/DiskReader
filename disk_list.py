import psutil


def disk_list():
    # function that retrun a list of disks
    devices = [] # list only with name of user's devices(disks)
    disk = []
    disklist = psutil.disk_partitions(all=False)  # list with user data(How many disks does he have)
    for disk in disklist:
        # print(disks.device)
        devices.append(disk.device)
    return print(f"Список дисков:{devices}") # return the list with disks we need
    # Seconde variaton of code
    # i = 0
    # while i<len(a):
    #     # print(a[i])
    #     c = a[i]
    #     b.append(c.device) # тут на каждой итерации добавляем в список нужный нам объект
    #     i += 1


print(disk_list())
