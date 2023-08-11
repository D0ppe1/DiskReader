import psutil


def disk_list():
    '''
    function that retrun a list of disks
    :return: list of disks
    '''
    # list only with name of user's devices(disks)
    devices = []
    # list with user data(How many disks does he have)
    disklist = psutil.disk_partitions(all=False)
    for disk in disklist:
        devices.append(disk.device)
        # This one is remove these (':\\') symbols  from list
        # It's necessary for disk_analisis because argument of func(only str without symbols)
        devices = [x.split(':\\')[0] for x in devices]
    return devices
