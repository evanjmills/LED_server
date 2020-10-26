import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor


while True:
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use('clam')

    temp = askcolor()
    print(temp[0])
    root.destroy()