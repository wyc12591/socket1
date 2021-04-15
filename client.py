'''
Description: Socket_Client
Author: 多多
Date: 2021-04-15 09:36:22
LastEditTime: 2021-04-15 09:39:16
LastEditors: 多多
'''
import socket
import sys

address = ('127.0.0.1', 5005)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(address)
except Exception:
    print('[!] Server not found or not open')
    sys.exit()
while True:
    trigger = input('Input: ')
    s.sendall(trigger.encode())
    data = s.recv(1024)
    data = data.decode()
    print('[Received]', data)
    if trigger == '###':
        break
s.close()
