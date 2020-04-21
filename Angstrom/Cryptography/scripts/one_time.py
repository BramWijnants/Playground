#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('misc.2020.chall.actf.co', 20301))
msg = clientsocket.recv(640)

no_flag_found = True

while no_flag_found:

    clientsocket.send(b'2\n')
    msg = clientsocket.recv(128)
    clientsocket.send(b'A\n')
    msg = clientsocket.recv(128).decode('UTF-8')

    if msg[:5] != 'Wrong':
        no_flag_found = False
        print(msg[:-1])
