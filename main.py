from tkinter import *

root = Tk()
root.title("Stimmungsthermometer")
root.iconbitmap("c:/temper/temper/IconThermometer.ico")
root.geometry("920x480")

def clicked_button():
    return

button = Button(root, text="Increase the Heat!", command=clicked_button)
button.pack()

root.mainloop()