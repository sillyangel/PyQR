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
    data = ""
    fill_color = fill_color_entry.get() or "black"
    back_color = back_color_entry.get() or "white"
    size = size_entry.get() or 300
    selected_type = selected_option.get()

    # Validate user input
    if selected_type == "Plain Text":
        data = data_entry.get().strip()
        if not data:
            messagebox.showerror("Error", "Please enter data for the QR code.")
            return
    elif selected_type == "Wifi":
        ssid = ssid_entry.get().strip()
        password = password_entry.get().strip()
        encryption = encryption_entry.get().strip() or "WPA"

        # Validate SSID input
        if not ssid:
            messagebox.showerror("Error", "Please enter the SSID for the Wifi QR code.")
            return

        # Generate Wifi QR code
        data = f"WIFI:T:{encryption};S:{ssid};P:{password};;"
    elif selected_type == "Phone Number":
        # TODO: Generate QR code for Phone Number
        pass
    elif selected_type == "vCard":
        # TODO: Generate QR code for vCard
        pass

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
    filename = f"qr_codes/{random.randint(0, 100000)}.png"
    qr_img.save(filename)

    # Print the filename in the console
    print(f"QR code generated and saved as {filename}")
    messagebox.showinfo("Success", f"QR code generated and saved as {filename}")


def set_window_icon(window):
    if sys.platform == "win32":
        icon_path = "icon.ico"
        window.iconbitmap(icon_path)
    elif sys.platform == "darwin":
        icon_path = "icon.icns"
        icon_path_expanded = os.path.expanduser(icon_path)
        if os.path.exists(icon_path_expanded):
            window.iconbitmap(icon_path_expanded)
    elif sys.platform.startswith("linux"):
        icon_path = "icon.png"
        window.iconphoto(True, tk.PhotoImage(file=icon_path))


def open_github_repo():
    webbrowser.open("https://github.com/sillyangel/PyQR")


# Create GUI window
window = tk.Tk()
window.title("QR Code Generator v1.1.1")
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

# Data input for Plain Text
data_label = tk.Label(window, text="Data:")
data_label.pack()
data_entry = tk.Entry(window)
data_entry.pack()

# Data inputs for Wifi
ssid_label = tk.Label(window, text="SSID (Wifi):")
ssid_label.pack()
ssid_entry = tk.Entry(window)
ssid_entry.pack()
password_label = tk.Label(window, text="Password (optional):")
password_label.pack()
password_entry = tk.Entry(window)
password_entry.pack()
encryption_label = tk.Label(window, text="Encryption (optional, default: WPA):")
encryption_label.pack()
encryption_entry = tk.Entry(window)
encryption_entry.pack()

# Hide Wifi inputs by default
ssid_label.pack_forget()
ssid_entry.pack_forget()
password_label.pack_forget()
password_entry.pack_forget()
encryption_label.pack_forget()
encryption_entry.pack_forget()

# Dropdown menu options
options = ['Plain Text', 'Wifi', 'Phone Number', 'vCard']
selected_option = tk.StringVar(window)
selected_option.set(options[0])  # Set the default selected option

dropdown_label = tk.Label(window, text="Select Type:")
dropdown_label.pack()

dropdown_menu = tk.OptionMenu(window, selected_option, *options)
dropdown_menu.pack()


def update_fields(*args):
    selected_type = selected_option.get()
    if selected_type == "Plain Text":
        data_label.pack()
        data_entry.pack()
        ssid_label.pack_forget()
        ssid_entry.pack_forget()
        password_label.pack_forget()
        password_entry.pack_forget()
        encryption_label.pack_forget()
        encryption_entry.pack_forget()
    elif selected_type == "Wifi":
        data_label.pack_forget()
        data_entry.pack_forget()
        ssid_label.pack()
        ssid_entry.pack()
        password_label.pack()
        password_entry.pack()
        encryption_label.pack()
        encryption_entry.pack()
    else:
        # TODO: Hide/show inputs for other options
        pass


selected_option.trace("w", update_fields)

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

# Window open and make sure no closing
window.mainloop()
