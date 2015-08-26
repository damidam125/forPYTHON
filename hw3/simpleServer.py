'''
#한번 receive하면 서버 종료
from socket import *
svrSock = socket(AF_INET, SOCK_STREAM)
svrSock.bind(('127.0.0.1', 3000))
svrSock.listen(1)
conn, addr = svrSock.accept()

recvBuf = conn.recv(1024)
print(len(recvBuf))
print(recvBuf)
'''

#메세지를 여러번 receive
from socketserver import ThreadingTCPServer, StreamRequestHandler
PORT = 2000
class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        conn = self.request
        print('connection from', self.client_address)
        buf = conn.recv(1024) #1024 byte를 receive
        if not buf:
            print('nothing')
        else :
            print(buf)

server = ThreadingTCPServer(('127.0.0.1', 2000), MyRequestHandler)
print('listening on port', PORT)
server.serve_forever()