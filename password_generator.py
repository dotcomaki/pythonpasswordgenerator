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
    result_label.config(text="Random Password: " + random_password)

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("300x150")

style = ttk.Style()
style.configure("TButton", padding=5, font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 12))

length_label = ttk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = ttk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
