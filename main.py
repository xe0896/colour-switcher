from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import calc
import subprocess
import platform

def open():
    if platform.system() == "Windows":
        import os
        os.startfile('output.png')
    elif platform.sytem() == "Darwin":
        subprocess.run(["open", 'output.png'])
    else:
        subprocess.run(["xdg-open"], 'output.png')

def calculate(*args):
    try:
        value = 'zigzag.png'
        R = int(r.get())
        G = int(g.get())
        B = int(b.get())
        calc.process(value, R, G, B)
    except ValueError:
        pass
    display_image('output.png')

def display_image(image_path):
    image = Image.open(image_path)
    image = image.resize((700, 700), Image.Resampling.LANCZOS)
    screenshot = ImageTk.PhotoImage(image)
    image_label.config(image=screenshot)
    image_label.image = screenshot  # Prevent garbage collection

root = Tk()
root.title("Color Switcher")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1) 

# Input frame to keep input fields together
input_frame = ttk.Frame(mainframe)
input_frame.grid(column=1, row=1, columnspan=4, sticky=W)

# Labels for the input fields
ttk.Label(input_frame, text="R:").grid(column=1, row=1, sticky=W)
r = StringVar()
r_entry = ttk.Entry(input_frame, width=7, textvariable=r)
r_entry.grid(column=2, row=1, padx=5)

ttk.Label(input_frame, text="G:").grid(column=3, row=1, sticky=W)
g = StringVar()
g_entry = ttk.Entry(input_frame, width=7, textvariable=g)
g_entry.grid(column=4, row=1, padx=5)

ttk.Label(input_frame, text="B:").grid(column=5, row=1, sticky=W)
b = StringVar()
b_entry = ttk.Entry(input_frame, width=7, textvariable=b)
b_entry.grid(column=6, row=1, padx=5)

# Button below the input fields

button_frame = ttk.Frame(mainframe)
button_frame.grid(column=1, row=2, columnspan=6, sticky="ew")  # Full width

ttk.Button(button_frame, text="Calculate", command=calculate).pack(side="left")
ttk.Button(button_frame, text="Open", command=open).pack(side="right")

# Image display - placed in its own row below everything else
image_label = ttk.Label(mainframe)
image_label.grid(column=1, row=3, columnspan=1, pady=10)

# Configure grid weights to maintain layout
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(4, weight=1)
mainframe.rowconfigure(4, weight=1)

r_entry.focus()
root.bind("<Return>", calculate)

style = ttk.Style()
style.theme_use('clam') 

style.configure('TFrame', background='#1e1e1e')
style.configure('TLabel', background='#1e1e1e', foreground='white')
style.configure('TButton', background='#333333', foreground='white')

root.mainloop()