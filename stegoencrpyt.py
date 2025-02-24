import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def encrypt_message():
    def load_image():
        nonlocal selected_image_path
        selected_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if selected_image_path:
            messagebox.showinfo("Image Selected", f"Selected image: {selected_image_path}")

    def perform_encryption():
        message = message_entry.get()
        password = password_entry.get()
        if not message or not selected_image_path or not password:
            messagebox.showerror("Error", "Please enter a message, select an image, and provide a password.")
            return

        img = Image.open(selected_image_path)
        img = img.convert("RGB")
        data = img.getdata()

        # Check if the image is large enough to hold the message and password
        if len(message) * 8 + len(password) * 8 > len(data):
            messagebox.showerror("Error", "The image is too small to hold the message and password.")
            return

        new_data = []
        data_index = 0

        # Embed the password into the image first
        for char in password:
            for i in range(8):  # 8 bits for each character
                pixel = data[data_index]
                char_bit = (ord(char) >> (7 - i)) & 1
                new_pixel = (pixel[0] & ~1) | char_bit
                new_data.append((new_pixel, pixel[1], pixel[2]))  # Keep the green and blue channels unchanged
                data_index += 1

        # Embed the message into the image
        for char in message:
            for i in range(8):  # 8 bits for each character
                pixel = data[data_index]
                char_bit = (ord(char) >> (7 - i)) & 1
                new_pixel = (pixel[0] & ~1) | char_bit
                new_data.append((new_pixel, pixel[1], pixel[2]))  # Keep the green and blue channels unchanged
                data_index += 1

        # Create a new image with the modified data
        img.putdata(new_data)
        output_image_path = "encrypted_image.png"
        img.save(output_image_path)
        messagebox.showinfo("Success", f"Message encrypted and saved as '{output_image_path}'.")

    # Create the GUI
    encrypt_window = tk.Tk()
    encrypt_window.title("Encrypt Message")

    message_label = tk.Label(encrypt_window, text="Enter secret message:")
    message_label.pack(pady=5)
    message_entry = tk.Entry(encrypt_window, width=50)
    message_entry.pack(pady=5)

    password_label = tk.Label(encrypt_window, text="Enter password:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(encrypt_window, show='*', width=50)
    password_entry.pack(pady=5)

    image_label = tk.Label(encrypt_window, text="Select image:")
    image_label.pack(pady=5)
    image_button = tk.Button(encrypt_window, text="Browse", command=load_image)
    image_button.pack(pady=5)

    encrypt_button = tk.Button(encrypt_window, text="Encrypt", command=perform_encryption)
    encrypt_button.pack(pady=5)

    selected_image_path = ""
    encrypt_window.mainloop()

if __name__ == "__main__":
    encrypt_message()