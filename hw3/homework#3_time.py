__author__ = 'dami'

import datetime
import time
import random


def homework3() :
    dt = datetime.datetime(2015,8,9)
    delt = datetime.timedelta(minutes=1)

    while dt < datetime.datetime(2015,8,20):
        file_name = dt.strftime('%Y%m%d_DATA1')
        msg = ''
        for a in range(0,1440) :
            rand1 = random.randrange(0,9999)
            rand2 = random.randrange(0,9999)
            rand3 = random.randrange(0,9999)
            msg += str(dt).replace('-','').replace(':','').replace(' ', '')[0:12] \
                   + ', {0:4d}, {1:4d}, {2:4d}\n'.format(rand1, rand2, rand3)
            time.sleep(1/1000)
            dt += delt

        with open(file_name, 'a') as f:
            f.write(msg)

homework3()