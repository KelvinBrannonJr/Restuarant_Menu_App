import qrcode

# Make QR code from Django server host address
image = qrcode.make("https://127.0.0.1:8000")

# Save PNG image OF Django server host address
image.save("qr.png")
