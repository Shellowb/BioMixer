# -*- coding: utf-8 -*

import serial
import struct
from io import BytesIO


class MachineCmd(object):
    """
        define the structure of the data, little-endian
        h is for 2 byte integer, see the full list here https://docs.python.org/3/library/struct.html#format-characters
        add as many data types as you want to send to arduino

    """

    _struct = struct.Struct('<hhhh')

    def __init__(self, port='/dev/ttyUSB0'):
        self.arduino = serial.Serial(port, 9600)
        self.buffer = BytesIO()
        self.d1 = 0
        self.d2 = 0
        self.d3 = 0
        self.d4 = 0

    def serialize(self):
        self.buffer.write(self._struct.pack(self.d1, self.d2, self.d3, self.d4))

    @staticmethod
    def to_hex(data):
        return ":".join("{:02x}".format(c) for c in data)

    def set_values(self, d1=0, d2=0, d3=0, d4=0):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4

    def read(self, line=False, size=1):
        if line is True:
            return self.arduino.readline()
        else:
            return self.arduino.read(size=size)

    def write(self, message=''):
        if message == '':
            self.serialize()
            self.arduino.write(bytearray(self.buffer.getvalue()))
        else:
            self.arduino.write(message.encode('b'))
