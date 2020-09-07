from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Stimmungsthermometer")
root.iconbitmap("c:/temper/IconThermometer.ico")

thermo = ImageTk.PhotoImage(Image.open("Thermometer.png")) #.resize((450,660), Image.ANTIALIAS)
thermo_label = Label(image=thermo)
thermo_label.grid(row=0, column=0)

increaser_button = Button(root, text="Increase the Heat!")
increaser_button.grid(row=1, column=0)
decreaser_button = Button(root, text="Decrease the Heat!")
decreaser_button.grid(row=2, column=0)

root.mainloop()