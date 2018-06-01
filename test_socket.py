import socket
import ipdb


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.cjxh616.com',80))

s.send(b'GET / HTTP/1.1\r\nHost: www.cjxh616.com\r\nConnection: close\rn\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d.decode())
    else:
        break


data = ''.join(buffer)
print(data)
