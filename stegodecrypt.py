import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def decrypt_message():
    def load_image():
        nonlocal selected_image_path
        selected_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if selected_image_path:
            messagebox.showinfo("Image Selected", f"Selected image: {selected_image_path}")

    def perform_decryption():
        if not selected_image_path:
            messagebox.showerror("Error", "Please select an image.")
            return

        password = password_entry.get()
        if not password:
            messagebox.showerror("Error", "Please enter the password.")
            return

        img = Image.open(selected_image_path)
        img = img.convert("RGB")
        data = img.getdata()

        # Retrieve the password first
        password_bits = ""
        password_length = len(password) * 8
        for i in range(password_length):
            if i < len(data):
                pixel = data[i]
                password_bits += str(pixel[0] & 1)  # Get the least significant bit
            else:
                break

        # Convert password bits to characters
        retrieved_password = ""
        for i in range(0, len(password_bits), 8):
            byte = password_bits[i:i + 8]
            if len(byte) < 8:
                break
            retrieved_password += chr(int(byte, 2))

        # Check if the retrieved password matches the entered password
        if retrieved_password != password:
            messagebox.showerror("Error", "Incorrect password.")
            return

        # Now retrieve the message
        message = ""
        char_bits = ""
        for i in range(password_length, len(data) * 8):
            if i < len(data):
                pixel = data[i]
                char_bits += str(pixel[0] & 1)  # Get the least significant bit

                if len(char_bits) == 8:  # Every 8 bits form a character
                    message += chr(int(char_bits, 2))
                    char_bits = ""  # Reset for the next character

        messagebox.showinfo("Decrypted Message", f"Message: {message}")

    # Create the GUI
    decrypt_window = tk.Tk()
    decrypt_window.title("Decrypt Message")

    image_label = tk.Label(decrypt_window, text="Select image:")
    image_label.pack(pady=5)
    image_button = tk.Button(decrypt_window, text="Browse", command=load_image)
    image_button.pack(pady=5)

    password_label = tk.Label(decrypt_window, text="Enter password:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(decrypt_window, show='*', width=50)
    password_entry.pack(pady=5)

    decrypt_button = tk.Button(decrypt_window, text="Decrypt", command=perform_decryption)
    decrypt_button.pack(pady=5)

    selected_image_path = ""
    decrypt_window.mainloop()

if __name__ == "__main__":
    decrypt_message()