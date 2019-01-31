import serial
import io
import time
# Water, kitchen
ser = serial.Serial("/dev/ttyUSB0",9600, timeout= 0.5)
# powder
ser1 = serial.Serial("/dev/ttyACM1",9600, timeout= 0.5)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
#time.sleep(3)
def check_led():
    ser.write(b'c\n')
    ser.flush()
    """
    a = str(ser.readline())
    print("a =", a)
    ser.write(b'2')
    a = str(ser.readline())
    print("a =", a)
    ser.write(b'0')
    ser.write(b'0')
    ser.write(b'e')
    ser.write(b'c')
    a = str(ser.readline())
    print("a =", a)"""

def turn_on_pot():
    ser.write(b'be\n')
    ser.flush()
    ser.write(b'c')
    #print(ser.readline())
    ser.flush()

def show():
    ser.write(b'c\n')
    a= str(ser.readline())
    c = float(a[2])
    c = c + float(a[4])/10 + float(a[5])/100
    print(a)
    return c

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