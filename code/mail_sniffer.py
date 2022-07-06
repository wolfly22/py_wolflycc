import imp
from itertools import count
from scapy.all import sniff

def packet_callback(packet):
    print(packet.show())

def main():
    sniff(prn=packet_callback,count=1)

if __name__=="__main__":
    main()