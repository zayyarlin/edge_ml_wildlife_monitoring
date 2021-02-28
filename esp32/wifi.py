import network
import urequests as requests
import ujson

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('', '')


url = "https://firestore.googleapis.com/v1/projects/global-wildlife-listening/databases/(default)/documents/detections"

# Ideally should be this form
# data = {'type':'mcu test 3', 'detection_time':'2021-02-13T13:21:00Z'}
#udata = ujson.dumps(data)

dataStr = """
{
  "fields": {
    "type": {
      "stringValue": "mcu test 3"
    }
  }
}
"""
headers = {'Content-Type': 'application/json'}
r = requests.post(url, headers=headers, data=dataStr)
r.close()

print('done')