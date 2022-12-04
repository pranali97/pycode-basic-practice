import time

def myfunc():
    start_time = time.time()
    print(start_time)

myfunc()

import getpass
print(getpass.getuser())  #usernsme


import os
print(os.environ['PATH'])


import sys
print(sys.version)
print(sys.version_info)

import datetime

now = datetime.datetime.now()

print(now)
print(now.strftime("%y-%m-%d %H:%M:%S"))

d =  datetime.date(2022,9,19)
print(d)

today = datetime.date.today()
print(today.weekday())
print(today.isoweekday())

tdelta = datetime.timedelta(days=7)
nine_days_from_now = today - tdelta
print(nine_days_from_now)

my_birthday = datetime.date(2022,11,25)
tday =  my_birthday - today
print(tday.total_seconds())

time_of_day = datetime.time(3,34,27,100000)
print(time_of_day.microsecond)

full_datetime = datetime.datetime(2020,12,26,3,23,45,120000)
print(full_datetime.day)

ddelta = datetime.timedelta(days=10)

# print(full_datetime + ddelta)


dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

