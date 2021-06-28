import eel
import io
import pyqrcode
from base64 import b64encode
import png

@eel.expose

def generate_qr(data):
    img = pyqrcode.create(data)
    buffers = io.BytesIO()
    img.png(buffers, scale=6)
    encoded = b64encode(buffers.getvalue()).decode("ascii")
    print("QR code generation successful.")
    return "data:image/png;base64, " + encoded

#eel start html page with size
if __name__ == "__main__":
    eel.init("web")
    eel.start("index.html", size=(800,600), port=8080, mode='chrome')