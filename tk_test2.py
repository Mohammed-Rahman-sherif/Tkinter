from tkinter import *
from tkinter import ttk

window = Tk()
window.title("ComboBox")

def click():
	out = 'This is the value selected : ' + cmb.get()
	label2.configure(text = out)

window.geometry('1000x500')

label1 = Label(window, text = 'select option ', font = ('Arial', 15))
label1.grid(row = 0, column = 0)

label2 = Label(window, font = ('Arial', 15))
label2.grid(row = 4, column = 0)

btn = Button(window, text = 'click me', command = click)
btn.grid(row = 1, column = 1)

cmb = ttk.Combobox(window)
cmb['values'] = ('1','2','3')
cmb.current(0)
cmb.grid(row = 0, column = 1)

window.mainloop()