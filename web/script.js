function generate() {
    var data = document.getElementById('data').value
    console.log("Converting " + data + " to QR Code .....")
    eel.generate_qr(data)(setImage)
}
function setImage(base64) {
    document.getElementById('qr').src = base64
}
