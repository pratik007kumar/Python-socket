#!/usr/bin/env python3

import socket
import sys

HOST = ""  # Standard loopback interface address (localhost)
PORT = 17091        # Port to listen on (non-privileged ports are > 1023

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind((HOST, PORT))
while 1:
    print "Listen to " + str(PORT)
    srv.listen(1)             
    sock, addr = srv.accept()
    while 1:
        pal = sock.recv(2048)
        if not pal: 
            break
        print "Recieved %s:%s:" % addr, pal
        #lap = write_message(pal)
        print pal
    sock.close()
