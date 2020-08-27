import eel
import serial
import sys

eel.init('web')

@eel.expose
def add():
    print('ok')

eel.start("home.html", size = (800,600))