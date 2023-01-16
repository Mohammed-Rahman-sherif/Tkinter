from tkinter import *

window = Tk()
window.title('radio buttons')
window.geometry('500x500')

out = IntVar();

dot1 = Radiobutton(window, text ='option1', font = ('Arial', 15), value = 0, variable = out)
dot1.grid(row = 0, column = 0,sticky = 'W')

dot2 = Radiobutton(window, text ='option2', font = ('Arial', 15), value = 1, variable = out)
dot2.grid(row = 1, column = 0, sticky = 'W')

dot3 = Radiobutton(window, text ='option3', font = ('Arial', 15), value = 2, variable = out)
dot3.grid(row = 2, column = 0, sticky = 'W')

label1 = Label(window, textvariable = out)
label1.grid(row = 4, column = 0, sticky ='E', padx = 40)

window.mainloop()