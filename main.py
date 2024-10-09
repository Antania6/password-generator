import tkinter as tk

def generate_password(length):
    password = ''
    for _ in range(length):
        r = int(93 * (ord(id(_)) % 100) / 100) + 33
        password += chr(r)
    return password

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())

root = tk.Tk()
root.title("Random Password Generator")

length_label = tk.Label(root, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=lambda: password_entry.delete(0, tk.END) or password_entry.insert(0, generate_password(int(length_entry.get()))))
generate_button.pack()

password_entry = tk.Entry(root, width=40)
password_entry.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_password)
copy_button.pack()

root.mainloop()