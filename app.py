import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Hello World!")

root.geometry("300x150")
root.eval('tk::PlaceWindow . center')

label = tk.Label(root, text="Hello world, it's me Wassim", font=("Arial", 12))
label.pack(pady=10)

entry_lable = tk.Label(root, text="Enter your name")
entry_lable.pack()
entry= tk.Entry(root, width=30)
entry.pack(pady=10)

def on_button_click():
    name = entry.get()
    messagebox.showinfo(f"Hello {name}!")
button = tk.Button(root, text="Click on me", command=on_button_click, font=("Arial", 10))
button.pack(pady=10)

root.mainloop()