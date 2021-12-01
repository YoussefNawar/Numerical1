from tkinter import ttk
import tkinter.messagebox
import self as self

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
lbl = ttk.Label(window, text = "Enter the function ").grid(column = 0, row = 0)
func = tk.StringVar()
nameEntered = ttk.Entry(window, width = 12, textvariable = func).grid(column = 1, row = 0)
lb1 = ttk.Label(window,text="Choose the method ").grid(column = 0,row = 3)



def bisection_button():
    lb11 = ttk.Label(window, text="enter upper x:").grid(column=0, row=5)
    xu = tk.IntVar()
    xuEntered = ttk.Entry(window, width=12, textvariable=xu).grid(column=1, row=5)
    lb12 = ttk.Label(window, text="enter lower x:").grid(column=0, row=6)
    xl = tk.IntVar()
    xlEntered = ttk.Entry(window, width=12, textvariable=xl).grid(column=1, row=6)

    def goo():
        bisection(func.get(),xu.get(),xl.get())


    go = Button(window, text="go", activebackground="black", activeforeground="white", bg="grey", bd=10, command=goo).grid(column=0,row=7)

b0 = Button(window, text="bisection", activebackground="black", activeforeground="white", bg="grey", bd=10, command=bisection_button).grid(column=0,row=4)


def false():
    lb11 = ttk.Label(window, text="enter upper x:").grid(column=0, row=5)
    xu = tk.IntVar()
    xuEntered = ttk.Entry(window, width=12, textvariable=xu).grid(column=1, row=5)
    lb12 = ttk.Label(window, text="enter lower x:").grid(column=0, row=6)
    xl = tk.IntVar()
    xlEntered = ttk.Entry(window, width=12, textvariable=xl).grid(column=1, row=6)

    def goo():
        falsi(func.get(), xu.get(), xl.get())

    go = Button(window, text="go", activebackground="black", activeforeground="white", bg="grey", bd=10,
                command=goo).grid(column=0, row=7)


b1 = Button(window, text="Regula-Falsi", activebackground="black", activeforeground="white", bg="grey", bd=10, command=false).grid(column=1,row=4)


def newton():
    lb11 = ttk.Label(window, text="enter  x0:").grid(column=0, row=5)
    x0 = tk.IntVar()
    x0Entered = ttk.Entry(window, width=12, textvariable=x0).grid(column=1, row=5)


    def goo():
        Newton(func.get(),  x0.get())

    go = Button(window, text="go", activebackground="black", activeforeground="white", bg="grey", bd=10,
                command=goo).grid(column=0, row=7)


b2 = Button(window, text="Newton-Raphson", activebackground="black", activeforeground="white", bg="grey", bd=10, command=newton).grid(column=3,row=4)


def fixed1():
    lb11 = ttk.Label(window, text="enter  x0:").grid(column=0, row=5)
    x0 = tk.IntVar()
    x0Entered = ttk.Entry(window, width=12, textvariable=x0).grid(column=1, row=5)
    lb12 = ttk.Label(window, text="enter  g(x):").grid(column=0, row=6)
    gx = tk.StringVar()
    gEntered = ttk.Entry(window, width=12, textvariable=gx).grid(column=1, row=6)

    def goo():
        fixed(func.get(), gx.get(), x0.get())

    go = Button(window, text="go", activebackground="black", activeforeground="white", bg="grey", bd=10,
                command=goo).grid(column=0, row=7)

b3 = Button(window, text="Fixed-Point", activebackground="black", activeforeground="white", bg="grey", bd=10, command=fixed1).grid(column=4,row=4)


def secant1():
    lb11 = ttk.Label(window, text="enter upper x:").grid(column=0, row=5)
    xu = tk.IntVar()
    xuEntered = ttk.Entry(window, width=12, textvariable=xu).grid(column=1, row=5)
    lb12 = ttk.Label(window, text="enter lower x:").grid(column=0, row=6)
    xl = tk.IntVar()
    xlEntered = ttk.Entry(window, width=12, textvariable=xl).grid(column=1, row=6)

    def goo():
        secant(func.get(), xu.get(), xl.get())

    go = Button(window, text="go", activebackground="black", activeforeground="white", bg="grey", bd=10,
                command=goo).grid(column=0, row=7)


b4 = Button(window, text="secant", activebackground="black", activeforeground="white", bg="grey", bd=10, command=secant1).grid(column=5,row=4)






window.mainloop()

