from tkinter import *  # Import everything from the Tkinter library. no need to install this library
root = Tk()  # Create the main application window (root window)
print(root)  # Print the reference of the Tkinter window object in the console
root.mainloop()  # Start the Tkinter event loop to keep the window open
#/////////////////////////////////////////////////////////////////////////////////
from tkinter import *  # Import everything from the Tkinter library
root = Tk()  # Create the main application window (root window)
root.title("Age Calculator")  # Set the window title
root.geometry("400x400")  # Set window size as a string "widthxheight"
#root.resizeable(0,0) or root.resizable(width=False, height=False) to not allow people to expand GUI window
print(root)  # Print the reference of the Tkinter window object in the console
root.mainloop()  # Use root.mainloop() instead of mainloop()
#/////////////////////////////////////////////////////////////////////////////////
from tkinter import *  # Import everything from the Tkinter library
root = Tk()  # Create the main application window (root window)
root.title("Age Calculator")  # Set the window title
root.geometry("400x200")  # Set window size as a string "widthxheight"
#root.resizeable(0,0) or root.resizable(width=False, height=False) to not allow people to expand GUI window

lb1 = Label(root, text = "Your Name").grid(row=1, column=1, padx=90)  # Creates a Label widget with the text "Your Name" and places it in row 1, column 1 with 90 pixels of horizontal padding.
lb2 = Label(root, text = "Year of Birth").grid(row=2, column=1, padx=90)  # Creates a Label widget with the text "Year" and places it in row 2, column 1 with 90 pixels of horizontal padding.
lb3 = Label(root, text = "Month").grid(row=3, column=1, padx=90)  # Creates a Label widget with the text "Month" and places it in row 3, column 1 with 90 pixels of horizontal padding.
lb4 = Label(root, text = "Day").grid(row=4, column=1, padx=90)  # Creates a Label widget with the text "Day" and places it in row 4, column 1 with 90 pixels of horizontal padding.
#note: a better way to write the labels above may be following:
#lb1 = Label(root, text="Your Name")
#lb1.grid(row=1, column=1, padx=90)

#note: padx=90 adds horizontal padding (extra space) on both sides of the widget. It means there will be 90 pixels of empty space to
# the left and right of the label. This helps in adjusting the layout and making the UI look better.

root.mainloop()  # Use root.mainloop() instead of mainloop()
#////////////////////////////////////////////////////////////////////////////////////
from tkinter import *  # Import everything from the Tkinter library
root = Tk()  # Create the main application window (root window)
root.title("Age Calculator")  # Set the window title
root.geometry("400x200")  # Set window size as a string "widthxheight"
lb1 = Label(root, text = "Your Name" ).grid(row=1, column=1, padx=90)
lb2 = Label(root, text = "Year" ).grid(row=2, column=1, padx=90)
lb3 = Label(root, text = "Month").grid(row=3, column=1, padx=90)
lb4 = Label(root, text = "Day" ).grid(row=4, column=1, padx=90)
#note: padx=90 adds horizontal padding (extra space) on both sides of the widget. It means there will be 90 pixels of empty space to
# the left and right of the label. This helps in adjusting the layout and making the UI look better.

NameVariable = StringVar()  # Creates a StringVar variable to store the input value from the Name entry field.
YearVariable = StringVar()  # Creates a StringVar variable to store the input value from the Year entry field.
MonthVariable = StringVar()  # Creates a StringVar variable to store the input value from the Month entry field.
DayVariable = StringVar()  # Creates a StringVar variable to store the input value from the Day entry field.

EntryName = Entry(root, textvariable=NameVariable).grid(row=1, column=2)  # Creates an Entry field for name input, links it to NameVariable, and places it in row 1, column 2.
EntryYear = Entry(root, textvariable=YearVariable).grid(row=2, column=2)  # Creates an Entry field for year input, links it to YearVariable, and places it in row 2, column 2.
EntryMonth = Entry(root, textvariable=MonthVariable).grid(row=3, column=2)  # Creates an Entry field for month input, links it to MonthVariable, and places it in row 3, column 2.
EntryDay = Entry(root, textvariable=DayVariable).grid(row=4, column=2)  # Creates an Entry field for day input, links it to DayVariable, and places it in row 4, column 2.


root.mainloop()  # Use root.mainloop() instead of mainloop()
