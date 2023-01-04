from tkinter import *
from PIL import ImageTk, Image
from matplotlib import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from numpy.core.function_base import linspace

root = Tk()
root.title("Graph")
root.iconbitmap("favicon.ico")
root.resizable(False, False)

varlegend = StringVar()
vargrid = StringVar()

fig = Figure(figsize=(3,3), dpi=100)
a = fig.add_subplot(111)

def graph():
    """Function responsible for plotting the graph. 
    0 arguments
    
    1. Taking ranges of x,y. If input is empty, they are set to basic values.
    2. Replacing string form with numpy equivalent.
    3. Setting attributes and plotting the graph. """
    list = (function.get()).split(";")

    try:
        x1 = eval(rangex1.get())
    except:
        x1 = 0
    try:
        x2 = eval(rangex2.get())
    except:
        x2 = 10
    try:
        y1 = eval(rangey1.get())
    except:
        y1 = -10
    try:
        y2 = eval(rangey2.get())
    except:
        y2 = 20
    
    x = linspace(x1, x2)

    a.clear()
    a.set_ylim(y1, y2)
    a.set_xlim(x1, x2)
    a.set_xlabel(labelx.get())
    a.set_ylabel(labely.get())
    a.set_title(title.get())

    for i in list:
        i = i.replace("sin", "np.sin")
        i = i.replace("cos", "np.cos")
        i = i.replace("tan", "np.tan")
        i = i.replace("ctan", "1/np.tan")
        i = i.replace("pi", "np.pi")
        i = i.replace("e", "np.e")
        i = i.replace("sqrt", "np.sqrt")
        i = i.replace("ln", "np.log")
        i = i.replace("log10", "np.log10")
        i = i.replace("^", "**")

        f = eval("lambda x: " + i)
        y = f(x)
        
        a.plot(x, y, label=i)

    if varlegend.get() == "On":
        a.legend()
    if vargrid.get() == "On":
        a.grid()

    canvas.draw()


def click(sth):
    """Function that inserts the clicked value into Entry (formula).
    1 argument - button symbol - str"""
    current = function.get()
    function.delete(0, END)
    function.insert(0, str(current) + str(sth))

def delete():
    """Function that deletes last symbol in Entry (formula).
    0 arguments"""
    current = function.get()
    function.delete(0, END)
    function.insert(0, str(current)[:-1])

def clear():
    """Function that deletes all the symbols in Entry (formula).
    0 arguments"""
    function.delete(0, END)

def info():
    """Function that opens a new window with basic information about the program.
    0 arguments"""
    info = Toplevel()
    info.resizable(False, False)
    info.title("Graph - Information")
    info.iconbitmap("favicon.ico")
    txt = Label(info, font=7, justify=LEFT, text = "O PROGRAMIE\n\nProgram rysuje wykresy podanych\nfunkcji. Należy je oddzielać znakiem ';'.\nObowiązkowe jest wpisanie wzoru\nfunkcji. Zakresy x,y przybiorą wartośći\ndomyślne.")
    txt.pack()
    binfook = Button(info, text="OK", padx=5, borderwidth=3, command=info.destroy)
    binfook.pack(side=BOTTOM, pady=5)


#--------- FRAMES ---------#
frame1 = LabelFrame(root, text="Function", padx=10, pady=10)
frame1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
frame10 = LabelFrame(frame1, padx=10, pady=10)
frame10.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
frame11 = LabelFrame(frame1, text= "X axis", padx=10, pady=10)
frame11.grid(row=1, column=0, padx=10, pady=10)
frame12 = LabelFrame(frame1, text= "Y axis", padx=10, pady=10)
frame12.grid(row=1, column=1, padx=10, pady=10)

frame2 = LabelFrame(root, text="", padx=10, pady=28)
frame2.grid(row=1, column=0, padx=10, pady=10, sticky="W")
frame3 = LabelFrame(root, text="", padx=10, pady=20)
frame3.grid(row=1, column=1, padx=10, pady=10, sticky="E")
frame5 = LabelFrame(root, borderwidth=0)
frame5.grid(row=2, column=0, columnspan=2, padx=5, sticky="E")


#--------- MENU ---------#
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Start", command=graph)
filemenu.add_command(label="Quit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)

infomenu = Menu(menubar, tearoff=0)
infomenu.add_command(label="Show info", command=info)
menubar.add_cascade(label="Info", menu=infomenu)


#--------- FORMULA ---------#
label1 = Label(frame10, text="Formula")
label1.grid(row=0, column=0)
function = Entry(frame10, font=13, width=43)
function.grid(row=0, column=1)

#--------- TITLE ---------#
label2 = Label(frame10, text="Title")
label2.grid(row=1, column=0)
title = Entry(frame10, font=13, width=43)
title.grid(row=1, column=1)

#--------- LEGEND & GRID ---------#
c1 = Checkbutton(frame10, text="Legend", variable=varlegend, onvalue="On", offvalue="Off")
c1.deselect()
c1.grid(row=0, column=2)
c2 = Checkbutton(frame10, text="Grid", variable=vargrid, onvalue="On", offvalue="Off")
c2.deselect()
c2.grid(row=1, column=2)


#--------- X AXE ---------#
labelx = Entry(frame11, font=13, width=21)
labelx.grid(row=0, column=1, columnspan=3)
labelxl = Label(frame11, text="Label")
labelxl.grid(row=0, column=0)
rangex1 = Entry(frame11, font=13, width=9)
rangex1.grid(row= 1, column=1)
rangex2 = Entry(frame11, font=13, width=9)
rangex2.grid(row= 1, column=3)
labelfrom1 = Label(frame11, text="from")
labelfrom1.grid(row=1, column=0)
labelto1 = Label(frame11, text="to")
labelto1.grid(row=1, column=2)

#--------- Y AXE ---------#
labely = Entry(frame12, font=13, width=21)
labely.grid(row=0, column=1, columnspan=3)
labelyl = Label(frame12, text="Label")
labelyl.grid(row=0, column=0)
rangey1 = Entry(frame12, font=13, width=9)
rangey1.grid(row=1, column=1)
rangey2 = Entry(frame12, font=13, width=9)
rangey2.grid(row= 1, column=3)
labelfrom2 = Label(frame12, text="from")
labelfrom2.grid(row=1, column=0)
labelto2 = Label(frame12, text="to")
labelto2.grid(row=1, column=2)


#--------- CANVAS ---------#
canvas = FigureCanvasTkAgg(fig, frame3)
canvas.get_tk_widget().grid(row=0, column=0)


#--------- BUTTONS ---------#
b0 = Button(frame2, text="0", width=5, height=4, bg="lightgrey", command=lambda: click(0))
b1 = Button(frame2, text="1", width=5, height=4, bg="lightgrey", command=lambda: click(1))
b2 = Button(frame2, text="2", width=5, height=4, bg="lightgrey", command=lambda: click(2))
b3 = Button(frame2, text="3", width=5, height=4, bg="lightgrey", command=lambda: click(3))
b4 = Button(frame2, text="4", width=5, height=4, bg="lightgrey", command=lambda: click(4))
b5 = Button(frame2, text="5", width=5, height=4, bg="lightgrey", command=lambda: click(5))
b6 = Button(frame2, text="6", width=5, height=4, bg="lightgrey", command=lambda: click(6))
b7 = Button(frame2, text="7", width=5, height=4, bg="lightgrey", command=lambda: click(7))
b8 = Button(frame2, text="8", width=5, height=4, bg="lightgrey", command=lambda: click(8))
b9 = Button(frame2, text="9", width=5, height=4, bg="lightgrey", command=lambda: click(9))
b0.grid(row=3, column=1)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=0, column=0)
b8.grid(row=0, column=1)
b9.grid(row=0, column=2)
bdot = Button(frame2, text=".", width=5, height=4, command=lambda: click("."))
bdot.grid(row=3, column=2)
bscolon = Button(frame2, text=";", width=5, height=4, command=lambda: click(";"))
bscolon.grid(row=3, column=0)

bplus = Button(frame2, text="+", width=5, height=4, command=lambda: click("+"))
bplus.grid(row=0, column=3)
bminus = Button(frame2, text="-", width=5, height=4, command=lambda: click("-"))
bminus.grid(row=1, column=3)
bmult = Button(frame2, text="*", width=5, height=4, command=lambda: click("*"))
bmult.grid(row=2, column=3)
bdiv = Button(frame2, text="/", width=5, height=4, command=lambda: click("/"))
bdiv.grid(row=3, column=3)

bl = Button(frame2, text="(", width=5, height=4, command=lambda: click("("))
bl.grid(row=0, column=4)
br = Button(frame2, text=")", width=5, height=4, command=lambda: click(")"))
br.grid(row=1, column=4)
bpi = Button(frame2, text="pi", width=5, height=4, command=lambda: click("pi"))
bpi.grid(row= 2, column= 4)
be = Button(frame2, text="e", width=5, height=4, command=lambda: click("e"))
be.grid(row= 3, column= 4)

bsin = Button(frame2, text="sin", width=5, height=4, command=lambda: click("sin"))
bsin.grid(row=0, column=5)
bcos = Button(frame2, text="cos", width=5, height=4, command=lambda: click("cos"))
bcos.grid(row=1, column=5)
btan = Button(frame2, text="tan", width=5, height=4, command=lambda: click("tan"))
btan.grid(row=2, column=5)
bctan = Button(frame2, text="ctan", width=5, height=4, command=lambda: click("ctan"))
bctan.grid(row=3, column=5)

bsqrt = Button(frame2, text="sqrt", width=5, height=4, command=lambda: click("sqrt"))
bsqrt.grid(row=0, column=6)
bln = Button(frame2, text="ln", width=5, height=4, command=lambda: click("ln"))
bln.grid(row=1, column=6)
blog10 = Button(frame2, text="log10", width=5, height=4, command=lambda: click("log10"))
blog10.grid(row=2, column=6)
bdel = Button(frame2, text="delete", bg="orange", width=5, height=4, command=delete)
bdel.grid(row=3, column=6)


bstart = Button(frame5, text="Start", relief="groove", command=graph)
bstart.grid(row=0, column=0, padx=5, pady=10, sticky="E")
bclear = Button(frame5, text="Clear", relief="groove", command=clear)
bclear.grid(row=0, column=1, padx=5, pady=10, sticky="E")
binfo = Button(frame5, text="Info", relief="groove", command=info)
binfo.grid(row=0, column=2, padx=5, pady=10, sticky="E")
bquit = Button(frame5, text="Quit", relief="groove", command=quit)
bquit.grid(row=0, column=3, padx=5, pady=10, sticky="E")


root.config(menu=menubar)
root.mainloop()


# funkcja odwrotna 

# obsluga ctan, symbol pi, mozna uzywac ^ zamiast **, przyciski clear i delete