from tkinter import *
from tkinter.ttk import *
from Update import Update_Window

def click_save():
    dic = dict(zip(["5 минут", "15 минут", "30 минут", "1 час", "2 часа"],[5,15,30,60,120]))
    rates = []
    for i in (eur,usd,gbr,jpy,cny):
        if i.get() > 0:
            rates.append(i.get())
    a = comb.get()
    upd_time = dic[a]
    Update_Window(upd_time, rates)

windowSet = Tk()
windowSet.title("Настройки")
windowSet.geometry('400x250')

frm = Frame(windowSet, height=300, width=300)
frm.pack()

frm_rates = LabelFrame(frm, text = "Выберите валюту", relief=RIDGE)
frm_rates.grid(row=0, column=0, sticky=W, padx=20, pady=20)

eur = IntVar()
eur.set(1)
usd = IntVar()
usd.set(0)
gbr = IntVar()
gbr.set(-1)
jpy = IntVar()
jpy.set(-2)
cny = IntVar()
cny.set(-3)

eurCB = Checkbutton(frm_rates, text='EUR', var = eur, onvalue = 1, offvalue = 0).pack(anchor=W)
usdCB = Checkbutton(frm_rates, text='USD', var = usd, onvalue = 2, offvalue = 0).pack(anchor=W)
gbrCB = Checkbutton(frm_rates, text='GBR', var = gbr, onvalue = 3, offvalue = 0).pack(anchor=W)
jpyCB = Checkbutton(frm_rates, text='JPY', var = jpy, onvalue = 4, offvalue = 0).pack(anchor=W)
cnyCB = Checkbutton(frm_rates, text='CNY', var = cny, onvalue = 5, offvalue = 0).pack(anchor=W)

frm_update = LabelFrame(frm, text = "Выберите частоту обновления", relief=RIDGE)
frm_update.grid(row=0, column=1, sticky=E, padx=20, pady=20)

comb = Combobox(frm_update)
comb['values'] = ('5 минут', "15 минут", "30 минут", "1 час", "2 часа")
comb.current(0)  # установите вариант по умолчанию
comb.pack()

frm_save = Frame(frm)
frm_save.grid(row=1, column=1, sticky=E, padx=20, pady=20)

btn = Button(frm_save, text = 'Save', command = click_save)
btn.pack(anchor = E)

windowSet.mainloop()