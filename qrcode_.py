import qrcode
img = qrcode.make("http://192.168.1.24:8080/#/")
with open('a.png', 'wb') as f:
    img.save(f)

