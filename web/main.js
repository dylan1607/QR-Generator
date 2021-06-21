generate = () => {
    var data = document.getElementById('data').value;
    eel.generate_qr(data)(setImage)
}
setImage = (base64) => {
    document.getElementById('qr').src = base64
}