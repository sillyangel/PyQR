import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import sys
import os
import webbrowser


def generate_qr_code():
    # Get user input from GUI
    data = data_entry.get().strip()
    fill_color = fill_color_entry.get() or "black"
    back_color = back_color_entry.get() or "white"
    size = size_entry.get() or 300

    # Validate user input
    if not data:
        messagebox.showerror("Error", "Please enter data for the QR code.")
        return

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)
    qr_img = qr_img.resize((int(size), int(size)), Image.LANCZOS)

    # Convert QR code image to PhotoImage
    qr_img_tk = ImageTk.PhotoImage(qr_img)

    # Update QR code image in GUI
    qr_label.configure(image=qr_img_tk)
    qr_label.image = qr_img_tk

    # Create a folder named "qr_codes" if it doesn't exist
    if not os.path.exists("qr_codes"):
        os.makedirs("qr_codes")

    # Save QR code image
    filename = f"qr_codes/{random.randint(0, 100000)}_{data}.png"
    qr_img.save(filename)

    # Print the filename in the console
    print(f"QR code generated and saved as {filename}")
    messagebox.showinfo("Success", f"QR code generated and saved as {filename}")


def set_window_icon(window):
    icon_path = "icon.ico"
    window.iconbitmap(icon_path)


def open_github_repo():
    webbrowser.open("https://github.com/sillyangel/PyQR")


# Create GUI window
window = tk.Tk()
window.title("QR Code Generator")
window.geometry("294x500")
set_window_icon(window)

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=sys.exit)

help_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="GitHub Repository", command=open_github_repo)

data_label = tk.Label(window, text="Data:")
data_label.pack()
data_entry = tk.Entry(window)
data_entry.pack()

fill_color_label = tk.Label(window, text="Fill Color (optional):")
fill_color_label.pack()
fill_color_entry = tk.Entry(window)
fill_color_entry.pack()

back_color_label = tk.Label(window, text="Background Color (optional):")
back_color_label.pack()
back_color_entry = tk.Entry(window)
back_color_entry.pack()

size_label = tk.Label(window, text="Image Size (optional):")
size_label.pack()
size_entry = tk.Entry(window)
size_entry.pack()

generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

qr_label = tk.Label(window)
qr_label.pack(pady=10)

window.mainloop()
