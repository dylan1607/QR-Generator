import io
import eel
import io
import pyqrcode
from base64 import b64encode

@eel.expose

def generate_qr(data):
    img = pyqrcode.create(data)
    buffers = io.BytesIO()
    img.png(buffers, scale=8)
    encoded = b64encode(buffers.getvalue()).decode("ascii")
    print("QR code generation successful.")
    return "data:image/png;base64, " + encoded

# Custom option
my_option = {
    'mode': 'chrome-app',
    'host': 'localhost',
    'port': 8080
}

#eel start html page with size
if __name__ == "__main__":
    eel.init("web")
    eel.start("index.html", size = (800,600))