import qrcode
from PIL import Image
import random
import os
import webbrowser


def generate_qr_code():
    # Get user input from console
    data = input("Enter data for the QR code: ").strip()
    fill_color = input("Enter fill color (optional, default is black): ") or "black"
    back_color = input("Enter background color (optional, default is white): ") or "white"
    size = input("Enter image size (optional, default is 300): ") or 300

    # Validate user input
    if not data:
        print("Error: Please enter data for the QR code.")
        return

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)
    qr_img = qr_img.resize((int(size), int(size)), Image.LANCZOS)

    # Save QR code image
    if not os.path.exists("qr_codes"):
        os.makedirs("qr_codes")

    filename = f"qr_codes/{random.randint(0, 100000)}.png"
    qr_img.save(filename)

    # Print the filename in the console
    print(f"QR code generated and saved as {filename}")


def open_github_repo():
    webbrowser.open("https://github.com/sillyangel/PyQR")


print("QR Code Generator V1.0.1")
print("Type 'exit' to quit.")
print("--------------------")

while True:
    command = input("Enter command (generate, help): ")

    if command == "generate":
        generate_qr_code()
    elif command == "help":
        print("Commands:")
        print("generate - Generate a QR code")
        print("help     - Open the GitHub repository for help")
    elif command == "exit":
        break
    else:
        print("Invalid command. Type 'help' for a list of commands.")
