from tkinter import *
from tkinter import messagebox as msg 
import sqlite3

window = Tk()
window.title("testing the frame1")
window.geometry('1920x1080')

Name = StringVar()
Password = StringVar()

####################################################

def login():
	conn = sqlite3.connect('test.db')
	cursor = conn.cursor()
	Na = str(Name.get())
	pwd = str(Password.get())
	print('name : ', Na)
	print('pwd', pwd)
	print('select Name from usertable1 where Name = ? and Password = ?', (Na, pwd))
	cursor.execute('select Name from usertable1 where Name = ? and Password = ?', (Na, pwd))
	result = cursor.fetchall();
	print('res',result)
	print(len(result))

	if len(result) == 0:
		msg.showinfo("Error message", 'Login Failed', icon = 'warning')
	else:
		msg.showinfo("confirmation message", 'Login Successful', icon = 'info')
	cursor.close()

'''	for data in result:
		print('data',data)
		print(len(result))
		if len(data) <= 0:
			print('Failed')
			msg.showinfo("Error message", 'Login Failed', icon = 'warning')
		if len(data) > 0:
			msg.showinfo("confirmation message", 'Login Successful', icon = 'info')'''
		
#	cursor.close()

def cancel():
	window.destroy()

####################################################

frame1 = Frame(window, width = 500)
frame1.pack(side = TOP)

label1 = Label(frame1, text = "Welcome Dear User!", font = ('Times New Roman', 25), fg = "red", bg = "white")
label1.grid(row = 0, column = 1, padx = 10, pady = 10)


frame2 = Frame(window, width = 1000)
frame2.pack(side = TOP)

label3 = Label(frame2, text = "Name", font = ('Times New Roman', 15), fg = "blue", bg = "white")
label3.grid(row = 1, column = 0, padx = 10, pady = 10)

tb3 = Entry(frame2, textvariable = Name, font = ('Times New Roman', 15))
tb3.grid(row = 1, column = 1, padx = 10, pady = 10)

label6 = Label(frame2, text = "Password", font = ('Times New Roman', 15), fg = "blue", bg = "white")
label6.grid(row = 3, column = 0, padx = 10, pady = 10)

tb6 = Entry(frame2, textvariable = Password, font = ('Times New Roman', 15))
tb6.grid(row = 3, column = 1, padx = 10, pady = 10)

###################################################

btn1 = Button(frame2, text = 'Submit', command = login, bg = 'green')
btn1.grid(row = 6, column = 0, padx = 50, pady = 5)

btn2 = Button(frame2, text = 'cancel', command = cancel, bg = 'red')
btn2.grid(row = 6, column = 1, padx = 50, pady = 5)

window.mainloop()