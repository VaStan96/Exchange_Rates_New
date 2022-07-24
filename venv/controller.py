from tkinter import *
from tkinter.ttk import *
from datetime import datetime, timedelta
import scrapp

global req_time, rates, str_rates


class MainWindow(Tk):
    def __init__(self, req_time, rates, str_rates):
        self.title("Актуальные курсы валют")
        self.geometry('400x250')
        self.req_time = req_time
        self.str_rates = str_rates

        frm1 = Frame(self,relief=RAISED, borderwidth=5)
        frm1.pack(fill=BOTH, expand=True)

        frm2 = Frame(self,relief=RAISED, borderwidth=5)
        frm2.pack_propagate(False)
        frm2.pack(fill=BOTH, expand=True, side=BOTTOM)

        lbl = Label(frm1, text=str_rates, font="TimesNewRoman, 16")
        lbl.pack(side=LEFT, anchor=NW)

        img = PhotoImage(file=r"C:\Users\vasta\PycharmProjects\Exchange_Rates\gear.png")

        btn = Button(frm1, image=img, command=open_settings)
        #btn = Button(frm1, text='Set', command=self.open_settings)
        btn.pack(side=RIGHT, anchor=NE)

        lbl_time = Label(frm2, text='Следующее обновление в ' + req_time, font="TimesNewRoman, 12")
        lbl_time.pack(side=LEFT, anchor=SW)



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

        #close_settings(req_time, str_rates)

def tink_rates(rates):
    dic = {}
    for elem in rates:
        dic[elem] = 100
    return dic

def open_settings(req_time, rates, str_rates):
    app.destroy()
    window = SettingsWindow(req_time, rates, str_rates)
    window.mainloop()

def close_settings():
    window.destroy()
    main()

def main (req_time, rates, str_rates):
    app = MainWindow(req_time, rates, str_rates)
    app.mainloop()

if __name__ == '__main__':
    req_time = datetime.now().strftime("%H:%M:%S")
    str_rates = "Пусто"
    rates = []
    main(req_time, rates, str_rates)