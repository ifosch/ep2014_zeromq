#!/usr/bin/env python
import zmq
import time

context = zmq.Context()

socket = context.socket(zmq.DEALER)

socket.connect('tcp://127.0.0.1:5555')
for i in range(10):
    socket.send(str(i))
    print socket.recv()
