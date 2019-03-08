"""
Main settings and functions to work from the server to Arduino Devices.
By: Marcelo Becerra A.
marcelo.becerra@ug.uchile.cl
"""
import serial
import io
import time

# Water, kitchen Arduino Port
ser = serial.Serial("/dev/ttyUSB0",9600, timeout= 0.5)

# powder Arduino Port
ser1 = serial.Serial("/dev/ttyACM1",9600, timeout= 0.5)


sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
#time.sleep(3)

# Testing Arduino led
def check_led():
    ser.write(b'c\n')
    ser.flush()

# Turn on the kitchen
def turn_on_pot():
    ser.write(b'be\n')
    ser.flush()
    ser.write(b'c')
    #print(ser.readline())
    ser.flush()

# Show information from serial port
def show():
    ser.write(b'c\n')
    a= str(ser.readline())
    c = float(a[2])
    c = c + float(a[4])/10 + float(a[5])/100
    print(a)
    return c

# Send Proportions of materials to the machine
def send_proportions(agar,water,glyc):
    start='a'
    end = 'e'
    wq = start + str(water) + end
    wq = wq.encode('utf-8')
    aq = start + str(agar) + end
    aq = aq.encode('utf-8')
    gq = start + str(glyc) + end
    gq = gq.encode('utf-8')
    print(wq, aq, gq)
    ser.write(wq)
    #ser.write(aq)
    #ser.write(gq)
