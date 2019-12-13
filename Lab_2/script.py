import smbus
import time
import json
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
bus = smbus.SMBus(1)
address = 0x29
arr = [7, 8, 18, 16, 15, 13, 12, 11]

bus.write_byte(address, 0xa0)
bus.write_byte(address, 0x03)
time.sleep(3)

while True:
    bus.write_byte(address, 0xac)
    a = bus.read_byte(address)
    bus.write_byte(address, 0xad)
    b = bus.read_byte(address)
    c = a + b*256
    print(c)
    time.sleep(0.1)

    if c < 100:
        for i in arr[:5]:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, False)
    elif c < 300:
        for i in arr[:3]:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, False)
    elif c >= 300:
        for i in arr:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, True)

    with open('test_data.txt', 'a+') as file1:
        dct = dict()
        dct['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        dct['value'] =  c
        json.dump(dct, file1)
        file1.write('\n')

    time.sleep(30)
