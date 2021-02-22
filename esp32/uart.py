from machine import UART
import time

uart = UART(2, tx=26, rx=25)
uart.init(115200, bits=8, parity=None, stop=1)

i = 0
while True:
    i += 1
    uart.write("hello from uart " + str(i) + "\n")
    time.sleep(1)
    if uart.any() > 0:
        print(uart.read())
    