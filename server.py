'''
Description: Socket_Server
Author: 多多
Date: 2021-04-15 09:31:38
LastEditTime: 2021-04-15 09:36:17
LastEditors: 多多
'''
import socket
address = ('127.0.0.1', 5005)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(5)
conn, addr = s.accept()
print('[+] Connected with ', addr)
while True:
    data = conn.recv(1024)
    data = data.decode()
    if not data:
        break
    print('[Received]', data)
    send = input('Input: ')
    conn.sendall(send.encode())
conn.close()
s.close()
