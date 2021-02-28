import time
import network
import urequests as requests
import ujson
from machine import UART

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('', '')
print('network connected')

url = 'https://firestore.googleapis.com/v1/projects/global-wildlife-listening/databases/(default)/documents/events'
headers = {'Content-Type': 'application/json'}
move_dataStr = """
{
  "fields": {
    "type": {
      "stringValue": "move"
    }
  }
}
"""
stationary_dataStr = """
{
  "fields": {
    "type": {
      "stringValue": "stationary"
    }
  }
}
"""

uart = UART(2, tx=26, rx=25)
uart.init(460800, bits=8, parity=None, stop=1)

# Store last state, if different send, else no needs to post
last_class_label = -1
while True:
    time.sleep(0.5)
    if uart.any() > 0:
        data_uart_str = uart.read().decode('UTF-8')
        data_uart_str = data_uart_str.replace('\n','')
        try:
            data = ujson.loads(data_uart_str)
        except:
            print('JSON parse error ' + data_uart_str)
        class_label = data['Classification']
        if class_label != last_class_label:
            if class_label == 2:
                dataStr = stationary_dataStr
            else:
                dataStr = move_dataStr
            r = requests.post(url, headers=headers, data=dataStr)
            r.close()
            last_class_label = class_label