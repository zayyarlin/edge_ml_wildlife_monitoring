from machine import UART
import time
import ujson

uart = UART(2, tx=26, rx=25)
#uart.init(115200, bits=8, parity=None, stop=1)
uart.init(460800, bits=8, parity=None, stop=1)

i = 0
while True:
    time.sleep(1)
    if uart.any() > 0:
        data_str = uart.read().decode('UTF-8')
        data_str = data_str.replace("\n","")
        print('read : ' + data_str)
        try:
            data = ujson.loads(data_str)
            print(data['Classification'])
        except:
            print('Parse failed')
    