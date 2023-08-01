import psutil

b = psutil.disk_usage('/')
print(b)
