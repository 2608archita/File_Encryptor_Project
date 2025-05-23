import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import hashlib
import os

def get_key_from_password(password):
    hashed = haslib.sha256(password.encode()).digest()
    return Fernet(base64.urlsafe_b64encode(hashed))

def get_fernet(password):
    key = hashlib.sha256(password.encode()).digest()
    import base64
    return Fernet(base64.urlsafe_b64encode(key))

def encrypt_file_gui():
    file_path = filedialog.askopenfilename()
    password = password_entry.get()

    if not file_path or not password:
        messagebox.showwarning("Missing","File and password required!")
        return

    try:
        fernet = get_fernet(password)
        with open(file_path,"rb") as file:
            data = file.read()
        encrypted = fernet.encrypt(data)
        new_file = file_path + ".enc"
        with open(new_file, "wb") as file:
            file.write(encrypted)
        messagebox.showinfo("Success",f"File encrypted:\n{new_file}")
    except Exception as e:
        messagebox.showerror("Error",str(e))

def decrypt_file_gui():
    file_path = filedialog.askopenfilename()
    password = password_entry.get()

    if not file_path or not password:
        messagebox.showwarning("Missing","File and password required!")
        return
    try:
        fernet = get_fernet(password)
        with open(file_path,"rb") as file:
            encrypted_data = file.read()
        decrypted = fernet.decrypt(encrypted_data)
        new_file = "decrypted_" + os.path.basename(file_path).replace(".enc", "")
        with open(new_file, "wb") as file:                       
            file.write(decrypted)
        messagebox.showinfo("Success",f"File decrypted:\n{new_file}")
    except Exception as e:
        messagebox.showerror("Error", "Decryption failed.Wrong password or corrupted file.")

app = tk.Tk()
app.title("File Encryption & Decryption Tool")
app.geometry("400x250")

tk.Label(app, text="Enter Password:").pack(pady=10)
password_entry = tk.Entry(app, show="*", width=30)
password_entry.pack(pady=5)

tk.Button(app, text="Encrypt file", command=encrypt_file_gui, bg="green",fg="white").pack(pady=10)
tk.Button(app, text="Decrypt file", command=decrypt_file_gui, bg="blue",fg="white").pack(pady=10)

tk.Label(app, text="Created by Archita").pack(side="bottom",pady=10)

app.mainloop()
        
