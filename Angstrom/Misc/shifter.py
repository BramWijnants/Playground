#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#calculate fibonacci
def fibo(nterms):
    n1, n2 = 0, 1
    count = 0
    if nterms == 0:
        return(n1)
    if nterms == 1:
       return(n2)
    else:
       while count < nterms:
           if (count == nterms-1):
               return n2
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1

#ceasar cipher encrypt
def encrypt(string, shift):
 
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  return cipher

if __name__ == '__main__':
   
    import socket 
   
    #connect to socket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('misc.2020.chall.actf.co', 20300))
    
    #recieve data, encode bytes to string and get P and n from message
    msg = clientsocket.recv(640).decode('UTF-8')
    p = msg[302:].split(' ')[0]
    n = int(msg[302:].split(' ')[2][2:-2])
    
    #calculate the shift based on n, encode p with the shift
    shift = fibo(n)
    enc_msg = str.encode(encrypt(p, shift)+'\n')
    clientsocket.send(enc_msg) # send message with "\n"
    
    msg2 = clientsocket.recv(640).decode('UTF-8') 
    
    # We need to do this 50 more times
    key_found = False
    
    while not key_found:
        
        p = msg2[6:].split(' ')[0]
        n = int(msg2.split(' ')[3][2:-2])
    
        shift = fibo(n)
        enc_msg = str.encode(encrypt(p, shift)+'\n')
        clientsocket.send(enc_msg)
        msg2 = clientsocket.recv(640).decode('UTF-8')
        
        if msg2[:4] != 'Shif':
            print(msg2[:-1])
            key_found = True
    