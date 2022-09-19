import tkinter
def knp(oponent):
	import random
	variki={1:'Папір',
	2:"Ножиці",
	3:"Колодязь"}
	z=random.randint(1, 3)
	if oponent=="Н" or 'н':
		oponent=2
	elif oponent=="П" or "п":
		oponent=1
	elif oponent=="К" or 'к':
		oponent=3
	else:
		print('Це шо? Я так не граю')
		e.insert('Це шо? Я так не граю')
	if variki[z]==variki[oponent]:
		e.delete(0, END)
		e.insert(0,'Нічия')
	elif (z==1 and oponent==3) or (z==2 and oponent==1) or (z==3 and oponent==2):
		e.delete(0, END)
		e.insert(0,'Ви програли! Опонент поставив: '+variki[z]+'. Ви поставили: '+variki[oponent])
	else:
		e.delete(0, END)
		e.insert(0,'Ви виграли! Опонент поставив: '+variki[z]+'. Ви поставили: '+variki[oponent])
from tkinter import * 

window = Tk()  
window.title("Highload")
e = Entry(window, width=70, borderwidth=7)
e.grid(row=0, column=0, columnspan=1, padx=10, pady=5)  
lbl = Label(window, text="Program", font=("Roboto Bold", 10))  
lbl.grid(column=0, row=2)  
btn = Button(window, text="Папір",padx=40, pady=20, command=lambda:knp('П'))
btn1 = Button(window, text="Ножиці", command=lambda:knp("Н"))
btn2 = Button(window, text="Колодязь", command=lambda:knp("К"))  
btn.grid(column=2, row=0)
btn1.grid(column=3, row=0)
btn2.grid(column=4, row=0)  
window.mainloop()