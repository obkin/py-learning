# You can work with date and time in Python:
import datetime

print(datetime.datetime.now()) # 2025-01-07 23:30:49.297879
print(datetime.datetime.today()) # 2025-01-07 23:30:49.297879

print(datetime.datetime.now().day) # 7
print(datetime.datetime.now().month) # 1
print(datetime.datetime.now().year) # 2025
print(datetime.datetime.now().hour) # 23

print(datetime.date.isoformat(datetime.date.today())) # 2025-01-07

print(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')) # 2025-01-07 23:30:49
