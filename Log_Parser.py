#!/usr/bin/python3


"""
This script is created to parse data in group of files.
Search can be done with the line of simple text or by regex.
"""


from tkinter.filedialog import askopenfilenames
from tkinter import *
import os
import re
files = []


def open_files():
    global files
    files = askopenfilenames()
    e1.delete(0, END)
    e1.insert(0, files)


def search():
    file_output = os.getcwd() + "\output.txt"
    out = open(file_output, 'w', encoding="utf-8")
    patern = e2.get()

    if not e1.get():
        exit()
    master.quit()
    if var1.get() == 0:
        for file_name in sorted(files, reverse=True):
            with open(file_name, mode='rb') as file:

                header = os.path.basename(file_name).split(".")[0] + "\n"
                str_output = ""
                for line in file:
                    line = line.decode(encoding="cp1251")
                    if patern in line:
                        str_output += line
                if str_output:
                    str_output = header + str_output
                    print(str_output, file=out)

    else:
        p = re.compile(patern)
        for file_name in sorted(files, reverse=True):
            with open(file_name, mode='rb') as file:

                header = os.path.basename(file_name).split(".")[0] + "\n"
                str_output = ""
                for line in file:
                    line = line.decode(encoding="cp1251")
                    if re.match(p, line):
                        str_output += line
                if str_output:
                    str_output = header + str_output
                    print(str_output, file=out)


master = Tk()

Label(master, text="Files").grid(row=0)
Label(master, text="Search str\nregex").grid(row=1)

e1 = Entry(master, width=50)
e2 = Entry(master, width=50)
b1 = Button(master, text='Open', command=open_files)
b2 = Button(master, text='OK', command=search)
b3 = Button(master, text='Quit', command=master.quit)

var1 = IntVar()
c1 = Checkbutton(master, text="regular", variable=var1)


e1.grid(row=0, column=1, pady=5)
e2.grid(row=1, column=1, pady=5)
b1.grid(row=0, column=3)
c1.grid(row=3)
b2.grid(row=3, column=3)
b3.grid(row=3, column=4)
mainloop()
