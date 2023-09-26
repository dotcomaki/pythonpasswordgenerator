import random
import string
import tkinter as tk
from tkinter import ttk

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password():
    password_length = int(length_entry.get())
    random_password = generate_random_password(password_length)
    
    # Clear any existing text in the text widget
    password_text.config(state=tk.NORMAL)  # Enable editing
    password_text.delete("1.0", tk.END)
    
    # Insert the generated password into the text widget
    password_text.insert(tk.END, random_password)
    
    # Disable editing again to make it read-only
    password_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("300x250")

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

password_text = tk.Text(root, wrap=tk.WORD, height=5, width=30)
password_text.grid(row=2, columnspan=2, padx=10, pady=10)
password_text.config(state=tk.DISABLED)  # Make the text widget read-only

# Start the GUI main loop
root.mainloop()
