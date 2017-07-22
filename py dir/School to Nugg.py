#College tuition cost in chicken nuggets#
#Imports#
from tkinter import *
import tkinter as tk
from math import *

#Text File for UI production#
Schools = open('Schools.txt', 'r')

#Splitting up the text file# 
def get_column_1(f):
    for line in f:
        yield line.split(',')[0]
def get_column_2(f):
    for line in f:
        yield line.split(',')[1]

#Gui window#
root = Tk()

#Window modifications#
root.title("Tuition to Nugg")
root.geometry("420x180")

mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 25, padx = 25)

#Name of School#
s_var = StringVar(root)
choices = get_column_1(Schools.readlines())
s_var.set("Choose a College")

popupMenu = OptionMenu(mainframe, s_var, *choices)
Label(mainframe, text="Colleges").grid(row = 1, column = 0)
popupMenu.grid(row = 1, column = 2)

#Numeber of years dropdown#
y_var = StringVar(root)
choices = {1, 2, 3, 4}
y_var.set(1)
 
popupMenu = OptionMenu(mainframe, y_var, *choices)
Label(mainframe, text="Number of Years").grid(row = 3, column = 0)
popupMenu.grid(row = 3, column = 2)

#Name of school selected to line number of text#
def School_line():
    Schools = open('Schools.txt', 'r')
    line_num = -1
    search_phrase = s_var.get()
    for line in Schools.readlines():
        line_num += 1
        if line.find(search_phrase) >= 0:
            return(line_num)

#Line number of School to line number of Cost#       
def Cost():
    Schools = open('Schools.txt', 'r')
    N_1 = (Schools.read(School_line()))
    N_2 = get_column_2(N_1)
    return N_2
    
#Enter button#           
def select():
    Number_of_Nuggets = "%s Nuggets" % print(Cost())
    print(Number_of_Nuggets)

button = tk.Button(mainframe, text = "Enter", command = select)
button.grid(row = 7, column = 1)

#Clean up#
Schools.close()
mainloop( )
root.mainloop()
