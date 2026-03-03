#AGE CALC
import datetime
from tkinter import * #import library
from tkinter.constants import LEFT

from PIL.ImImagePlugin import DATE

root = Tk() #create main app window (root window)
root.title("Age Calculator") #set window title
root.geometry("300x200") #set window size as string "widthxheight"
#root.resizeable(0,0) #allows NO expansion of GUI
#print(root) # Print the reference of the Tkinter window object in console

def apple():
    birthdate = datetime.datetime(int(YearVar.get()), int(MonthVar.get()), int(DayVar.get()))
    age = datetime.datetime.now() - birthdate
    convertdays =  int(age.days)
    convertyears = round(convertdays / 365, 2)
    Label(text = f"{NameVar.get()} your age is {convertyears} years old.").grid(row = 6, column = 1)


lb1 = Label(root, text="Your Name", anchor="w", width=15).grid(row=1, column=1)
lb2 = Label(root, text="Your Birth Year", anchor="w", width=15).grid(row=2, column=1)
lb3 = Label(root, text="Your Birth Month", anchor="w", width=15).grid(row=3, column=1)
lb4 = Label(root, text="Your Birth Day", anchor="w", width=15).grid(row=4, column=1)

NameVar = StringVar()
YearVar = StringVar()
MonthVar = StringVar()
DayVar = StringVar()

EntryName = Entry(root, textvariable = NameVar).grid(row = 1, column=2)
EntryYear = Entry(root,textvariable = YearVar).grid(row = 2, column=2)
EntryMonth = Entry(root, textvariable = MonthVar).grid(row = 3, column=2)
EntryDay = Entry(root, textvariable = DayVar).grid(row = 4, column=2)

button1 = Button(root, text= "Calculate Age", command = apple).grid(row =5, column = 1)
#button1 = Button(root, text = "Calculate Age")
#button1.grid(row=5, column = 1)

root.mainloop()
