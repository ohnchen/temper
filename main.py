from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Stimmungsthermometer")
root.iconbitmap("c:/temper/IconThermometer.ico")    

n = 1 
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

thermo_1 = ImageTk.PhotoImage(Image.open("Thermometer_1.png"))
thermo_2 = ImageTk.PhotoImage(Image.open("Thermometer_2.png"))
thermo_3 = ImageTk.PhotoImage(Image.open("Thermometer_3.png"))
thermo_4 = ImageTk.PhotoImage(Image.open("Thermometer_4.png"))
thermo_5 = ImageTk.PhotoImage(Image.open("Thermometer_5.png")) #.resize((450,660), Image.ANTIALIAS)
thermo_label = Label(image=thermo_1)
thermo_label.grid(row=0, column=0)

increaser_button = Button(root, text="Increase the Heat!", command=increase)
increaser_button.grid(row=1, column=0)
decreaser_button = Button(root, text="Decrease the Heat!", command=decrease)
decreaser_button.grid(row=2, column=0)

root.mainloop()