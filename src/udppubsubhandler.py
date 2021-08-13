import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 9000

class Pub:
    def __init__(self):
        self.sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
    def send(self,msg):
        self.sock.sendto(msg,(UDP_IP,UDP_PORT))
        print("message sent %s" %msg)

class Sub:
    def __init(self):
        print("subscriber initialised")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((UDP_IP,UDP_PORT))
        data,addr = self.sock.recvfrom(1024)
        print(" recieved message %s "%data)
        