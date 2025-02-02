import tkinter as tk

root = tk.Tk()
root.title("Hello world!")

lable = tk.Label(root, text="Hello world, it's me Wassim")
lable.pack()

button = tk.Button(root, text="Ckick on me", command=lambda: print("knappen trycktes"))
button.pack()

root.mainloop()