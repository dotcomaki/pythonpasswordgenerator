import random
import string
import tkinter as tk
from tkinter import ttk
import pyperclip

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password():
    password_length = int(length_entry.get())
    random_password = generate_random_password(password_length)
    
    # Copy the password to clipboard
    pyperclip.copy(random_password)
    
    result_label.config(text="Random Password: " + random_password)

    # Calculate the new window width based on password length
    new_width = max(300, len(random_password) * 12)  # Minimum width of 300 pixels

    # Adjust window size
    root.geometry(f"{new_width}x200")

    # Adjust font size based on password length
    font_size = max(12, 240 // len(random_password))  # Minimum font size of 12
    style.configure("TLabel", font=("Helvetica", font_size))

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("300x200")

# Configure style
style = ttk.Style()
style.configure("TButton", padding=5, font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 12))

# Create widgets
length_label = ttk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = ttk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=2, columnspan=2, padx=10, pady=10)

# Add a button to copy the password to clipboard
copy_button = ttk.Button(root, text="Copy to Clipboard", command=lambda: pyperclip.copy(result_label.cget("text")[16:]))
copy_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Start the GUI main loop
root.mainloop()
