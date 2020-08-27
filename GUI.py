import eel
import serial
import sys
import serial.tools.list_ports as sp

eel.init('web')

@eel.expose
def add():
    if sys.platform.startswith('win'):
            ports = sp.comports(include_links=False)
            for port in ports:
                if port.description.startswith('USB-ITN'):
                    port = port.device
                    ser = serial.Serial(port, 9600, timeout=1)
                    if ser.is_open:
                        ser.write(b"1\r")
                        response = ser.read(13)
                        a = response[6:12].decode()
                        
                else:
                    a = 'Not Found'
    return a

eel.start("home.html", size = (800,600))