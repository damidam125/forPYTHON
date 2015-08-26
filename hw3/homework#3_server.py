__author__ = 'dami'

import datetime
from socketserver import ThreadingTCPServer, StreamRequestHandler

PORT = 2003

class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        msg = []
        dt = datetime.datetime.now()
        while True:
            buf = self.request.recv(1024) #1024 byte를 receive
            if not buf and not msg:
                pass
            elif datetime.datetime.now() - dt < datetime.timedelta(seconds=5):
                msg.append(str(buf, 'utf-8'))
            else:
                print(msg.sort())
                msg = []
                dt = datetime.datetime.now()

            buf = b'' #empty the buf

server = ThreadingTCPServer(('127.0.0.1', PORT), MyRequestHandler)
print('listening on port', PORT)
server.serve_forever()
