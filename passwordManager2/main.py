import tkinter as tk
from tkinter import messagebox
import sqlite3
from cryptography.fernet import Fernet
import os
import hashlib

# Function to load or generate the encryption key
def load_or_generate_key():
    key_file = 'encryption_key.key'
    if os.path.exists(key_file):
        with open(key_file, 'rb') as file:
            key = file.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, 'wb') as file:
            file.write(key)
    return key

# Load the encryption key
key = load_or_generate_key()
cipher_suite = Fernet(key)

# Initialize SQLite database
conn = sqlite3.connect('passwords.db')
c = conn.cursor()

# Create tables if they don't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS passwords
             (site TEXT, username TEXT, encrypted_password TEXT)''')
conn.commit()

# Function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to encrypt a password
def encrypt_password(password):
    return cipher_suite.encrypt(password.encode('utf-8')).decode('utf-8')

# Function to decrypt a password
def decrypt_password(encrypted_password):
    return cipher_suite.decrypt(encrypted_password.encode('utf-8')).decode('utf-8')

# Function to add a password to the database
def add_password():
    site = site_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if site and username and password:
        encrypted_password = encrypt_password(password)
        c.execute("INSERT INTO passwords (site, username, encrypted_password) VALUES (?, ?, ?)",
                  (site, username, encrypted_password))
        conn.commit()
        messagebox.showinfo("Success", "Password added successfully!")
        site_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Function to display stored passwords
def display_passwords():
    display_window = tk.Toplevel(root)
    display_window.title("Stored Passwords")

    c.execute("SELECT site, username, encrypted_password FROM passwords")
    records = c.fetchall()

    for record in records:
        site, username, encrypted_password = record
        try:
            decrypted_password = decrypt_password(encrypted_password)
        except Exception as e:
            decrypted_password = "Decryption failed"

        site_label = tk.Label(display_window, text=f"Site: {site}")
        site_label.pack()

        username_label = tk.Label(display_window, text=f"Username: {username}")
        username_label.pack()

        password_label = tk.Label(display_window, text=f"Password: {decrypted_password}")
        password_label.pack()

        separator = tk.Label(display_window, text="-"*40)
        separator.pack()

# Function to verify login credentials
def verify_login():
    username = username_entry.get()
    password = hash_password(password_entry.get())

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()

    if result:
        login_window.destroy()
        show_main_menu()
    else:
        messagebox.showerror("Login Error", "Invalid username or password")

# Function to register a new user
def register_user():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if password != confirm_password:
        messagebox.showerror("Registration Error", "Passwords do not match")
        return

    hashed_password = hash_password(password)
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful! Please log in.")
        show_login_window()
    except sqlite3.IntegrityError:
        messagebox.showerror("Registration Error", "Username already exists")

# Function to show the main menu after successful login
def show_main_menu():
    global site_entry, username_entry, password_entry, root

    root = tk.Tk()
    root.title("Password Storage")

    # Labels and entries for site, username, and password
    site_label = tk.Label(root, text="Site Name:")
    site_label.grid(row=0, column=0, padx=10, pady=5)
    site_entry = tk.Entry(root, width=30)
    site_entry.grid(row=0, column=1, padx=10, pady=5)

    username_label = tk.Label(root, text="Username:")
    username_label.grid(row=1, column=0, padx=10, pady=5)
    username_entry = tk.Entry(root, width=30)
    username_entry.grid(row=1, column=1, padx=10, pady=5)

    password_label = tk.Label(root, text="Password:")
    password_label.grid(row=2, column=0, padx=10, pady=5)
    password_entry = tk.Entry(root, width=30)
    password_entry.grid(row=2, column=1, padx=10, pady=5)

    # Add and display buttons
    add_button = tk.Button(root, text="Add Password", command=add_password)
    add_button.grid(row=3, column=0, columnspan=2, pady=10)

    display_button = tk.Button(root, text="Display Passwords", command=display_passwords)
    display_button.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()

# Function to show the registration window
def show_register_window():
    global username_entry, password_entry, confirm_password_entry, register_window

    register_window = tk.Tk()
    register_window.title("Register")

    username_label = tk.Label(register_window, text="Username:")
    username_label.grid(row=0, column=0, padx=10, pady=5)
    username_entry = tk.Entry(register_window, width=30)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    password_label = tk.Label(register_window, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(register_window, width=30, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    confirm_password_label = tk.Label(register_window, text="Confirm Password:")
    confirm_password_label.grid(row=2, column=0, padx=10, pady=5)
    confirm_password_entry = tk.Entry(register_window, width=30, show="*")
    confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)

    register_button = tk.Button(register_window, text="Register", command=register_user)
    register_button.grid(row=3, column=0, columnspan=2, pady=10)

    register_window.mainloop()

# Function to show the login window
def show_login_window():
    global username_entry, password_entry, login_window

    login_window = tk.Tk()
    login_window.title("Login")

    username_label = tk.Label(login_window, text="Username:")
    username_label.grid(row=0, column=0, padx=10, pady=5)
    username_entry = tk.Entry(login_window, width=30)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    password_label = tk.Label(login_window, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(login_window, width=30, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    login_button = tk.Button(login_window, text="Login", command=verify_login)
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    login_window.mainloop()

# Check if any users exist
c.execute("SELECT * FROM users")
users_exist = c.fetchone()

# Show the appropriate window based on user existence
if users_exist:
    show_login_window()
else:
    show_register_window()

# Close the database connection when the application is closed
conn.close()
