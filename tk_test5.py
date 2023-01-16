from tkinter import *
from tkinter import messagebox as msg 

window = Tk()
window.title("Testing Background")
window.geometry('300x168+300+100')

img = PhotoImage(file = "circuit.png");
label1 = Label(window, image = img)
label1.place(x = 0, y = 0, relwidth = 1, relheight = 1)

window.mainloop()