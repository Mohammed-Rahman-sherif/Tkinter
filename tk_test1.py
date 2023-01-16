from tkinter import *

window = Tk()
window.title("scibot_game_controller")

label = Label(window, text = 'welcome dear gamer!!', font = ("Arial", 25))
label.grid(row = 0, column = 1)

label1 = Label(window, text = 'Type : ', font = ('Arial', 25))
label1.grid(row = 1, column = 0)

label2 = Label(window, font = ('Arial', 25))
label2.grid(row = 4, column = 0)

entry = Entry(window, width = 30)
entry.grid(row = 1, column = 1)

window.geometry('1000x500')

'''def click():
	s = 'the value is : ' + entry.get()
	label1.configure(text = s)'''

def click():
	out = 'The value is : ' + entry.get()
	label2.configure(text = out)

btn = Button(window, text = 'click me', font = ("Arial", 25), command = click)
btn.grid(row = 2, column = 1)





window.mainloop()