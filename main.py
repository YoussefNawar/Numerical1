from tkinter import ttk

import solutions
import sys
import tkinter
import tkinter as tk
import tkinter.font as font
from tkinter import *
from solutions import *

#solutions = {'Bisection': bisection(), 'Regula Falsi': falsi(),'Newton Raphson': Newton()}
window = Tk()
window.title('Numerical Methods for Root finding')
window.geometry('1500x800')
lbl = ttk.Label(window, text = "Enter the name:").grid(column = 0, row = 0)# Click event
def click():
    bisection(name.get(),1.111,0.9999)
name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 12, textvariable = name).grid(column = 0, row = 1)# Button widget
button = ttk.Button(window, text = "submit", command = click).grid(column = 1, row = 1)




window.mainloop()

