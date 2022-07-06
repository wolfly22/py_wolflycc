import struct as st
import ctypes as ct
import socket

class IP(ct.Structure):
    _fields_ = [
        ("ihl",          ct.c_ubyte,    4),
        ("version",      ct.c_ubyte,    4),
        ("tos",          ct.c_ubyte,    8),
        ("len",          ct.c_ushort,   16),
        ("id",           ct.c_ushort,   16),
        ("offset",       ct.c_ushort,   16),
        ("ttl",          ct.c_ubyte,    8),
        ("protocol_num", ct.c_ubyte,    8),
        ("sum",          ct.c_ushort,   16),
        ("src",          ct.c_uint,     32),
        ("dst",          ct.c_uint,     32)
    ]

    def __new__(cls,socket_buffer=None):
        return  cls.from_buffer_copy(socket_buffer)
    
    def __init__(self,socket_buffer=None):
        self.src_address = socket.inet_ntoa(st.pack("<L",self.src))
        self.dst_address = socket.inet_ntoa( st.pack("<L",self.dst))
        return 
