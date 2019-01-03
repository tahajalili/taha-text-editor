import sys
import os

v = sys.version
if "2.7" in v:
	from Tkinter import *
	import tkFileDialog

elif "3." in v:
	from tkinter import *
	from tkinter import filedialog
	

root = Tk()
root.title("TWEET SAVE")
input_text_area = Text(root)
input_text_area.grid(row=1, column=0, columnspan=4, sticky=N+S+E+W)
input_text_area.configure(background='#4D4D4D')

OPTIONS = ["Helvetica", 'Courier','arial', 'FreeMono']
variable = StringVar(root)
w = OptionMenu(root, variable, *OPTIONS)
w.grid()

def change_font():
	input_text_area.config(font=variable.get())

def exit():
	sys.exit()

def save_as():
	global input_text_area
	t = input_text_area.get("1.0", "end-1c")
	save_location = filedialog.asksaveasfilename(initialdir=os.getenv("HOME"))
	print(save_location)
	file1 = open(save_location,'w+')
	file1.write(t)
	file1.close()

button_change = Button(root, text='Change Font', command=change_font, height=1, width=8)
button_change.grid()

button_save = Button(root,text="Save", command=save_as, height=1, width=8)
button_save.grid()

button_exit = Button(root,text="Exit", command=exit, height=1, width=8)
button_exit.grid(column=0,row=10)

root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)
root.resizable(False,False)
root.mainloop()
