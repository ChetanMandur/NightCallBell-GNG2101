from bluedot.btcomm import BluetoothServer
from signal import pause
import gpiozero

led = gpiozero.LED(7)

s = BluetoothServer(data_received)

def data_received(data):
    led.on()
    #Speaker on
    
# while True:
    
