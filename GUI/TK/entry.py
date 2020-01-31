import tkinter as tk


window = tk.Tk()
label = tk.Label(text="Name")
label.pack()
entry = tk.Entry()
entry.pack()
name = entry.get()

window.mainloop()