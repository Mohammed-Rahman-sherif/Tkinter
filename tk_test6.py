from tkinter import *
from tkinter import messagebox as msg 
import sqlite3

window = Tk()
window.title("testing the frame1")
window.geometry('1920x1080')

#####################################################IGNORE#####################################################

img = PhotoImage(file = "bg.png");
label = Label(window, image = img)
label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#####################################################IGNORE ENDS#################################################

frame1 = Frame(window, width = 500)
frame1.pack(side = TOP)

label1 = Label(frame1, text = "Welcome Dear User!", font = ('Times New Roman', 25), fg = "red", bg = "white")
label1.grid(row = 0, column = 1, padx = 10, pady = 10)


frame2 = Frame(window, width = 1000)
frame2.pack(side = TOP)

label3 = Label(frame2, text = "Name", font = ('Times New Roman', 15), fg = "blue", bg = "white")
label3.grid(row = 1, column = 0, padx = 10, pady = 10)

tb3 = Entry(frame2, textvariable = 'Name', font = ('Times New Roman', 15))
tb3.grid(row = 1, column = 1, padx = 10, pady = 10)

label4 = Label(frame2, text = "ID", font = ('Times New Roman', 15), fg = "blue", bg = "white")
label4.grid(row = 2, column = 0, padx = 10, pady = 10)

tb4 = Entry(frame2, textvariable = 'ID', font = ('Times New Roman', 15))
tb4.grid(row = 2, column = 1, padx = 10, pady = 10)

label5 = Label(frame2, text = "E-mail", font = ('Times New Roman', 15), fg = "blue", bg = "white")
label5.grid(row = 3, column = 0, padx = 10, pady = 10)

tb5 = Entry(frame2, textvariable = 'E-mail', font = ('Times New Roman', 15))
tb5.grid(row = 3, column = 1, padx = 10, pady = 10)

label6 = Label(frame2, text = "Password", font = ('Times New Roman', 15), fg = "blue", bg = "white")
label6.grid(row = 4, column = 0, padx = 10, pady = 10)

tb6 = Entry(frame2, textvariable = 'Password', font = ('Times New Roman', 15))
tb6.grid(row = 4, column = 1, padx = 10, pady = 10)

label7 = Label(frame2, text = "Mobile No", font = ('Times New Roman', 15), fg = "blue", bg = "white")
label7.grid(row = 5, column = 0, padx = 10, pady = 10)

tb7 = Entry(frame2, textvariable = 'Mobile No', font = ('Times New Roman', 15))
tb7.grid(row = 5, column = 1, padx = 10, pady = 10)


window.mainloop()