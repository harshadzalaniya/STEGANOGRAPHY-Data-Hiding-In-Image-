# STEGANOGRAPHY Data-Hiding-In-Image
Steganogrphy is the process of hiding the important data in the Image or any file to make it secure while transferring the Information.
We can do this using python with the method of LSB(Least Significant Bit) which changes the Image size by making the small difference in the bits(pixels) of image while adding the secrete to Image. 

## Overview
This project uses robust LSB steganography to embed a secret message along with a passcode into an image. It consists of two Python scripts with user-friendly GUIs built using Tkinter.

## Features
- **Encryption:**  
  Embeds a secret message and passcode into `mypic.jpg` and saves the result as `encrypted.png`.

- **Decryption:**  
  Retrieves the hidden message from `encrypted.png` when the correct passcode is provided.

- **User-Friendly GUI:**  
  Easy-to-use interfaces for both encryption and decryption processes.

- **Robust Data Storage:**  
  Uses a header to store the lengths of the passcode and message for accurate extraction.
## Requirements
- Python 3.x(Suitable Version Of python)
- OpenCV  
- NumPy  
- Tkinter (usually included with Python)
## Installation

1. Clone the repository.
2. Install the required libraries:
   ```bash
   pip install opencv-python numpy
3. Place an image mypic.jpg in project directory
