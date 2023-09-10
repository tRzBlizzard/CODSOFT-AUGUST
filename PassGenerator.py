import tkinter as tk
import random
import string
from tkinter import ttk

def generate_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        password_result.config(text="Invalid length", fg="red")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))

    if password_length <= 1000:
        password_result.config(text=password, fg="green")
        password_scrollable.delete(1.0, tk.END)  # Clear previous text
        password_scrollable.insert(tk.END, password)
    else:
        password_result.config(text="Password is too long to display here.")
        password_scrollable.delete(1.0, tk.END)  # Clear previous text

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")  # Larger screen size

length_label = tk.Label(root, text="Password Length:", font=('Helvetica', 12), fg="blue")
length_label.pack()

length_entry = tk.Entry(root, font=('Helvetica', 12))
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=('Helvetica', 12), bg="orange")
generate_button.pack()

password_result = tk.Label(root, text="", font=('Helvetica', 14), fg="green")
password_result.pack()

# Scrollable text widget
password_scrollable = tk.Text(root, wrap=tk.WORD, font=('Helvetica', 14))
password_scrollable.pack(fill=tk.BOTH, expand=True)

root.mainloop()
