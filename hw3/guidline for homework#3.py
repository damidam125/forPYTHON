#guidline for homework#3
import time
import datetime
import random

dt_now = datetime.datetime.now()
dt_delta = datetime.timedelta(minutes=1)
dt_now
while True:
    dt_now = dt_now + dt_delta
    file_name = dt_now.strftime("%Y%m%d_DATA")
    data_time = dt_now.strftime("%Y%m%d%H%M")

    d1 = random.randrange(0, 9999)
    d2 = random.randrange(0, 9999)
    d3 = random.randrange(0, 9999)

    print(data_time)
    data = "{0}, {1:4d}, {2:4d}, {3:4d}\n".format(data_time, d1, d2, d3)

    with open(file_name, 'a') as f:
        f.write(data)
    time.sleep(1/100)