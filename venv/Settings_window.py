from tkinter import *
from tkinter.ttk import *
from datetime import datetime, timedelta
import scrapp

class SettingsWindow(Tk):
    def __init__(self, req_time, rates, str_rates):
        self.title("Настройки")
        self.geometry('400x250')

        frm = Frame(self, height=300, width=300)
        frm.pack()

        frm_rates = LabelFrame(frm, text="Выберите валюту", relief=RIDGE)
        frm_rates.grid(row=0, column=0, sticky=W, padx=20, pady=20)

        self.eur = IntVar()
        self.eur.set(1)
        self.usd = IntVar()
        self.usd.set(0)
        self.gbr = IntVar()
        self.gbr.set(-1)
        self.jpy = IntVar()
        self.jpy.set(-2)
        self.cny = IntVar()
        self.cny.set(-3)

        eurCB = Checkbutton(frm_rates, text='EUR', var=self.eur, onvalue=1, offvalue=0).pack(anchor=W)
        usdCB = Checkbutton(frm_rates, text='USD', var=self.usd, onvalue=2, offvalue=0).pack(anchor=W)
        gbrCB = Checkbutton(frm_rates, text='GBR', var=self.gbr, onvalue=3, offvalue=0).pack(anchor=W)
        jpyCB = Checkbutton(frm_rates, text='JPY', var=self.jpy, onvalue=4, offvalue=0).pack(anchor=W)
        cnyCB = Checkbutton(frm_rates, text='CNY', var=self.cny, onvalue=5, offvalue=0).pack(anchor=W)

        frm_update = LabelFrame(frm, text="Выберите частоту обновления", relief=RIDGE)
        frm_update.grid(row=0, column=1, sticky=E, padx=20, pady=20)

        comb = Combobox(frm_update)
        comb['values'] = ("5 минут", "15 минут", "30 минут", "1 час", "2 часа")
        comb.current(0)
        comb.pack()

        frm_save = Frame(frm)
        frm_save.grid(row=1, column=1, sticky=E, padx=20, pady=20)

        btn = Button(frm_save, text='Save', command=self.click_save)
        btn.pack(anchor=E)

    def click_save(self):
        dic = dict(zip(["5 минут", "15 минут", "30 минут", "1 час", "2 часа"], [5, 15, 30, 60, 120]))
        self.a = comb.get()
        req_time = datetime.now() + timedelta(minutes=dic[a])
        req_time = req_time.strftime("%H:%M:%S")

        rates = []
        for i in (eur, usd, gbr, jpy, cny):
            if i.get() > 0:
                rates.append(i.get())
        dic_rates = dict(zip([1, 2, 3, 4, 5], ['EUR', 'USD', 'GBR', 'JPY', 'CNY']))
        for elem in rates:
            elem = dic_rates[elem]
        rates = tink_rates(rates)
        for elem,val in rates:
            str_rates+= "1 "+elem+" = "+val+" RUB\n"
        print("__")
        # windowSet.destroy()
        # Update_Window(upd_time, rates)
        # return req_time, rates

if __name__ == '__main__':
    req_time = datetime.now().strftime("%H:%M:%S")
    str_rates = "Пусто"
    rates = []
    app = SettingsWindow(req_time, rates, str_rates)
    app.mainloop()