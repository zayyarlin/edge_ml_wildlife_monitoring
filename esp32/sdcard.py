import machine
import uos as os

sd = machine.SDCard(slot=2, width =1, sck=18, cs=4, mosi=23, miso=19)
os.mount(sd,'/sd')
os.chdir('/sd')

print(os.listdir())