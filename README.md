# File Encryption & Decryption Tool

This is a simple GUI-based tool built with Python and Tkinter for encrypting and decrypting files using password-based symmetric encryption (Fernet encryption from the cryptography library).

## Features

- Encrypt any file using a password.

- Decrypt encrypted files using the correct password.

- Simple and user-friendly interface built with Tkinter.


## Technologies Used

- Python 3

- Tkinter for GUI

- cryptography library for secure encryption/decryption

- hashlib for generating secure keys from passwords


## How It Works

A password is hashed using SHA-256 and encoded to create a Fernet-compatible key.

This key is then used to encrypt or decrypt the selected file.

Encrypted files are saved with a .enc extension.

Decrypted files are saved with a decrypted_ prefix.


## Requirements

- ### Python 3.x

- ### Required Python packages:

- cryptography

- tkinter (included with most Python installations)

-  To install the cryptography package, run:

```
pip install cryptography
```

## How to Run

1. Save the Python script.


2. Run the script using Python:
```bash
python file_encryption_tool.py
```


3. Enter your password in the GUI.


4. Click "Encrypt File" or "Decrypt File" and choose the file.



## Security Note

- Could you make sure to remember your password? If lost, files cannot be decrypted.

- This tool is for educational/personal use. Consider using more robust tools with key storage and management for sensitive data.



## Author

Created by Archita Sahoo
