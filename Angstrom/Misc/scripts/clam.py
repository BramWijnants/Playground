#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('misc.2020.chall.actf.co', 20204))

# msg = clientsocket.recv(6400)

clientsocket.send(b'clamclam\n')
msg = clientsocket.recv(64).decode('UTF-8')
print(msg)

        
        
