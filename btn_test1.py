from tkinter import *
from tkinter.ttk import *

canv = Tk()
canv.geometry('200x150')

#Create style object
sto = Style()

#configure style
sto.configure('TButton', font=
('calibri', 10, 'bold', 'underline'),
foreground='Green')
# button 1
btns = Button(canv, text='Welcome !',
      style='TButton',
      command=canv.destroy)

btns.grid(row=0, column=1, padx=50)

# button 2
btnns = Button(canv, text='Click to start !', command=None)
btnns.grid(row=1, column=1, pady=10, padx=50)

canv.mainloop()