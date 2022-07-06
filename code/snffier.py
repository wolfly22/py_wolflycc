from csv import Sniffer
from re import L
import socket
import os


host = socket.gethostbyname( socket.gethostname())

def main():
    socket_protocol = None
    if os.name == "nt":

        
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP
    
    snffier = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)
    snffier.bind((host,0))
    
    #设置数据包头
    snffier.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
    while True:
    #接收数据包
        if os.name == 'nt':
            snffier.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
        
        print(snffier.recvfrom(65565))

        if os.name=="nt":
            snffier.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)
    
if __name__ == "__main__":
    main()
