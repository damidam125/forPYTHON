__author__ = 'dami'
# client는 msg("time,<id>,<msg>") server에게 보냄(term<0.1)

import datetime
from time import sleep
from socket import *

svrSock = socket(AF_INET, SOCK_STREAM)
svrSock.connect(('127.0.0.1', 2003))
cnt = 0
td = datetime.now()

while td - datetime.datetime.now() < datetime.timedelta(seconds=1) :
    msg = datetime.datetime.now().strftime("%H%M%S") + ', client1 ' + str(cnt) + '  |  '
    encodedMsg = str.encode(msg)
    cnt += 1
    svrSock.send(encodedMsg)
    sleep(0.1)