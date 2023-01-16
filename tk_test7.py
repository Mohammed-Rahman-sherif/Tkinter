from tkinter import *
from tkinter import ttk

window = Tk()
window.title('FoToSo Play Console')
#window.iconbitmap('path')
window.geometry('500x200')

def check_checkbox () :
	if chk.get () == 1:
		btn1['state'] = 'normal'
	else:
		btn1['state'] = 'disabled'

def Accept():
	window.destroy()

def cancel():
	window.destroy()

def Next():
	window.destroy()
	window1 = Tk()
	window1.title('New Page')
	window1.geometry('500x500')

#############################PANE###############################
'''m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane")
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Label(m2, text="top pane")
m2.add(top)

bottom = Label(m2, text="bottom pane")
m2.add(bottom)'''

'''n = ttk.Notebook(parent)
f1 = ttk.Frame(n) # first page, which would get widgets gridded into it
f2 = ttk.Frame(n) # second page
77
n.add(f1, text='One')
n.add(f2, text='Two')'''

label1 = Label(window, text = 'Welcome Dear Gamer! ', font = ('Arial', 15), fg = 'green')
label1.grid(row = 0, column = 0)
label2 = Label(window, text = '   By marking tick in the checkbox, we assume that your accepting our terms and', font = ('Arial', 10), fg = 'blue')
label2.grid(row = 1, column = 0)
label3 = Label(window, text = '   conditions. Do not continue to use our FoToSo Play Console if you do not agree', font = ('Arial', 10), fg = 'blue')
label3.grid(row = 2, column = 0)
label4 = Label(window, text = '   to take all of the terms and conditions stated below. ', font = ('Arial', 10), fg = 'blue')
label4.grid(row = 3, column = 0)


chk = BooleanVar();

tick = Checkbutton(window, text = 'Accept Privacy Policy', font = ('Times New Roman', 10), command = check_checkbox, variable = chk, onvalue = 1, offvalue = 0)
tick.grid(row = 5, column = 0)

frame1 = Frame(window, width = 300, bg = 'white')
frame1.grid(row = 6, column = 0)

btn1 = Button(frame1, text = 'Next', command = Next, bg = 'green')
btn1['state'] = 'disabled'
btn1.grid(row = 1, column = 0, padx = 50, pady = 5)
btn2 = Button(frame1, text = 'Cancel', command = cancel, bg = 'red')
btn2.grid(row = 1, column = 1, padx = 50, pady = 5)

vertscroll = ttk.Scrollbar(window, orient=VERTICAL)
vertscroll.grid(column=3, row=0, sticky='NS')

window.mainloop()