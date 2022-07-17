from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from datetime import datetime

def click_btn():
    windowSet.mainloop()



window = Tk()
window.title("Актуальные курсы валют")
window.geometry('400x250')

frm1 = Frame(relief=RAISED, borderwidth=5)
frm1.pack(fill=BOTH, expand=True)

frm2 = Frame(relief=RAISED, borderwidth=5)
frm2.pack_propagate(False)
frm2.pack(fill=BOTH, expand=True, side = BOTTOM)

eur = 100
req_time = datetime.now().strftime("%H:%M:%S")

lbl = Label(frm1, text="1 EUR = "+str(eur)+" RUB", font = "TimesNewRoman, 16")
lbl.pack(side = LEFT, anchor = NW)

img = PhotoImage(file = r"C:\Users\vasta\PycharmProjects\Exchange_Rates\gear.png")

btn = Button(frm1, image = img, command = click_btn)
btn.pack(side = RIGHT, anchor = NE)

lbl_time = Label(frm2, font = "TimesNewRoman, 12")
lbl_time.pack(side = LEFT, anchor = SW)

window.mainloop()

