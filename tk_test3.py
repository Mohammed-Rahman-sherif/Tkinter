from tkinter import *

window = Tk()
window.title('check button')

window.geometry('500x500')

def click():
	out = 'Result : ' + format(chk.get())
	label1.configure(text = out)

chk = BooleanVar();

tick = Checkbutton(window, text = 'accept privacy policy', font = ('Arial', 15), command = click, variable = chk)
tick.grid(row = 0, column = 0)

label1 = Label(window, font = ('Arial', 15))
label1.grid(row = 2, column = 0)

window.mainloop()