# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:55:14 2022

@author: gabri
"""

#this program is a basic port scanner of the host machine that prints if a port is Open
#import the time and socket modules
import time
import socket 

#gets the host name of the machine
host = socket.gethostname()

#translates the hostname to IPv4 format
hostIP = socket.gethostbyname(host)

try:
    for port in range(0, 1023):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((hostIP, port))
        if result == 0:
            print(f'Port {port} is open.')
        else:
            print(f'Port {port} is closed or unknown.')
        sock.close()


except socket.error:
    print('Couldnt connect to server')


