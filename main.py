from tkinter import *
from PIL import ImageTk, Image

### Initialize the new TKinter window with an icon and a title
root = Tk()
root.title("Planspiel: Europa")
root.iconbitmap("c:/temper/IconThermometer.ico")    
root.geometry("320x410")

### Setting n to 1 so the "heat increases" at the first button push
n = 1 
### Defining the function for increasing the heat
def increase():
    global n 
    if n == 1:
        thermo_label.config(image=thermo_2)
        n += 1
    elif n == 2:
        thermo_label.config(image=thermo_3)
        n += 1 
    elif n == 3:
        thermo_label.config(image=thermo_4)
        n += 1 
    elif n == 4:
        thermo_label.config(image=thermo_5)
        n += 1
    else:
        thermo_label.config(image=thermo_5)

### Defining the function for decreasing the heat
def decrease():
    global n 
    if n == 5:
        thermo_label.config(image=thermo_4)
        n -= 1
    elif n == 4:
        thermo_label.config(image=thermo_3)
        n -= 1 
    elif n == 3:
        thermo_label.config(image=thermo_2)
        n -= 1 
    elif n == 2:
        thermo_label.config(image=thermo_1)
        n -= 1 
    else:
        thermo_label.config(image=thermo_1)

### Assinging the Images to variables
thermo_1 = ImageTk.PhotoImage(Image.open("Thermometer_1.png"))
thermo_2 = ImageTk.PhotoImage(Image.open("Thermometer_2.png"))
thermo_3 = ImageTk.PhotoImage(Image.open("Thermometer_3.png"))
thermo_4 = ImageTk.PhotoImage(Image.open("Thermometer_4.png"))
thermo_5 = ImageTk.PhotoImage(Image.open("Thermometer_5.png"))
thermo_label = Label(image=thermo_1)
thermo_label.grid(row=1, column=0)

### Putting buttons on the TK window with their ability to execute on of the two functions, also defining a title
title_lbl = Label(root, text="Stimmungsthermometer der ersten Partei:")
title_lbl.grid(row=0, column=0)
increaser_button = Button(root, text="Increase the Heat!", command=increase)
increaser_button.grid(row=2, column=0)
decreaser_button = Button(root, text="Decrease the Heat!", command=decrease)
decreaser_button.grid(row=3, column=0)

root.mainloop()