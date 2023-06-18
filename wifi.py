import qrcode

# Define the Wi-Fi network details
ssid = "Nachos"
password = "Nachos"
encryption = "WPA"  # Encryption type (e.g., WPA, WEP, None)

# Create a QR code instance
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)

# Set the data to be encoded as a Wi-Fi network
wifi_data = f"WIFI:S:{ssid};T:{encryption};P:{password};;"
qr.add_data(wifi_data)

# Generate the QR code
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image()

# Save the QR code image
img.save("wifi_qr_code.png")
