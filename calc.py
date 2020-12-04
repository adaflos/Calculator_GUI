#!/usr/bin/python

import Tkinter

x=0

top= Tkinter.Tk()

def number1click():
    x=1
    print(x)

def number2click():
    x=2
    print(x)

def number3click():
    x=3
    print(x)

def number4click():
    x=4
    print(x)

def number5click():
    x=5
    print(x)

def number6click():
    x=6
    print(x)

def number7click():
    x=7
    print(x)

def number8click():
    x=8
    print(x)

def number9click():
    x=9
    print(x)

def number0click():
    x=0
    print(x)

Button1 = Tkinter.Button(top, text="1", command=number1click, padx=10, pady=5)
Button1.pack()
Button2 = Tkinter.Button(top, text="2", command=number2click, padx=10, pady=5)
Button2.pack()
Button3 = Tkinter.Button(top, text="3", command=number3click, padx=10, pady=5)
Button3.pack()
Button4 = Tkinter.Button(top, text="4", command=number4click, padx=10, pady=5)
Button4.pack()
Button5 = Tkinter.Button(top, text="5", command=number5click, padx=10, pady=5)
Button5.pack()
Button6 = Tkinter.Button(top, text="6", command=number6click, padx=10, pady=5)
Button6.pack()
Button7 = Tkinter.Button(top, text="7", command=number7click, padx=10, pady=5)
Button7.pack()
Button8 = Tkinter.Button(top, text="8", command=number8click, padx=10, pady=5)
Button8.pack()
Button9 = Tkinter.Button(top, text="9", command=number9click, padx=10, pady=5)
Button9.pack()
Button0 = Tkinter.Button(top, text="0", command=number0click, padx=10, pady=5)
Button0.pack()

print(x)

top.mainloop()
