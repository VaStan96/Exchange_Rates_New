from tkinter import *
from tkinter.ttk import *
from datetime import datetime, timedelta
import scrapp
import threading, schedule, time
from pystray import MenuItem, Menu, Icon
from PIL import Image

class SettingsWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Настройки")
        self.geometry('400x250')

        frm = Frame(self, height=300, width=300)
        frm.pack()

        frm_rates = LabelFrame(frm, text="Выберите валюту", relief=RIDGE)
        frm_rates.grid(row=0, column=0, sticky=W, padx=20, pady=20)

        self.eur = StringVar()
        self.eur.set("EUR")
        self.usd = StringVar()
        self.usd.set("")
        self.gbp = StringVar()
        self.gbp.set("")
        self.jpy = StringVar()
        self.jpy.set("")
        self.cny = StringVar()
        self.cny.set("")

        eurCB = Checkbutton(frm_rates, text='EUR', var=self.eur, onvalue='EUR', offvalue="").pack(anchor=W)
        usdCB = Checkbutton(frm_rates, text='USD', var=self.usd, onvalue='USD', offvalue="").pack(anchor=W)
        gbrCB = Checkbutton(frm_rates, text='GBP', var=self.gbp, onvalue='GBP', offvalue="").pack(anchor=W)
        jpyCB = Checkbutton(frm_rates, text='JPY', var=self.jpy, onvalue='JPY', offvalue="").pack(anchor=W)
        cnyCB = Checkbutton(frm_rates, text='CNY', var=self.cny, onvalue='CNY', offvalue="").pack(anchor=W)

        frm_update = LabelFrame(frm, text="Выберите частоту обновления", relief=RIDGE)
        frm_update.grid(row=0, column=1, sticky=E, padx=20, pady=20)

        self.combVar = StringVar()
        self.combVar.set('')
        comb = Combobox(frm_update, textvariable=self.combVar)
        comb['values'] = ("5 минут", "15 минут", "30 минут", "1 час", "2 часа")
        comb.current(0)
        comb.pack()

        frm_save = Frame(frm)
        frm_save.grid(row=1, column=1, sticky=E, padx=20, pady=20)

        btn = Button(frm_save, text='Save', command=self.click_save)
        btn.pack(anchor=E)

    def click_save(self):
        dic = dict(zip(["5 минут", "15 минут", "30 минут", "1 час", "2 часа"], [5, 15, 30, 60, 120]))
        self.master.req_time = datetime.now() + timedelta(minutes=dic[self.combVar.get()])
        self.master.req_time = self.master.req_time.strftime("%H:%M")
        MainWindow.update_time = self.master.req_time
        MainWindow.update_minute = dic[self.combVar.get()]

        rates = []
        for i in (self.eur, self.usd, self.gbp, self.jpy, self.cny):
            if i.get() != "":
                rates.append(i.get())
        MainWindow.rates = rates
        rates = scrapp.Req(rates)
        self.master.str_rates = ""
        for elem,val in rates.items():
            self.master.str_rates+= "1 "+elem+" = "+str(val)+" RUB\n"

        self.master.lbl.config(text = self.master.str_rates)
        self.master.lbl_time.config(text='Следующее обновление в ' + self.master.req_time)
        self.destroy()
        Update(self.master.lbl, self.master.lbl_time)


class MainWindow(Tk):
    req_time = datetime.now().strftime("%H:%M")
    str_rates = "Выберите валюты"
    update_time = datetime.now() + timedelta(minutes=3)
    update_time = update_time.strftime("%H:%M")
    rates=['EUR']
    update_minute = 3

    def __init__(self):
        super().__init__()

        self.title("Актуальные курсы валют")
        self.geometry('400x250')
        #self.req_time = datetime.now().strftime("%H:%M")
        #self.str_rates = "Выберите валюты"

        frm1 = Frame(self,relief=RAISED, borderwidth=5)
        frm1.pack(fill=BOTH, expand=True)

        frm2 = Frame(self,relief=RAISED, borderwidth=5)
        frm2.pack_propagate(False)
        frm2.pack(fill=BOTH, expand=True, side=BOTTOM)

        self.lbl = Label(frm1, text=MainWindow.str_rates, font="TimesNewRoman, 16")
        self.lbl.pack(side=LEFT, anchor=NW)

        self.photo = PhotoImage(file=r"C:\Users\vasta\PycharmProjects\Exchange_Rates\gear.png")

        self.lbl_time = Label(frm2, text='Следующее обновление в ' + MainWindow.req_time, font="TimesNewRoman, 12")
        self.lbl_time.pack(side=LEFT, anchor=SW)

        thr1 = threading.Thread(target=Update, args=(self.lbl, self.lbl_time)).start()

        btn = Button(frm1, image=self.photo, command=self.open_settings)
        btn.pack(side=RIGHT, anchor=NE)


    def open_settings(self):
        window = SettingsWindow(self)
        window.grab_set()

def quit_window(icon, item):
    icon.stop()
    app.destroy()


def show_window(icon, item):
    icon.stop()
    app.after(0, app.deiconify)


def withdraw_window():
    app.withdraw()
    image = Image.open(r"C:\Users\vasta\PycharmProjects\Exchange_Rates\acc.ico")
    icon = Icon('main', image, 'Курс валют', menu=Menu(MenuItem('Показать', show_window), MenuItem('Закрыть', quit_window)))
    icon.run()

def Update(lbl, lbl_time):
    MainWindow.rates = scrapp.Req(MainWindow.rates)
    MainWindow.str_rates = ""
    for elem, val in MainWindow.rates.items():
        MainWindow.str_rates += "1 " + elem + " = " + str(val) + " RUB\n"

    lbl.config(text=MainWindow.str_rates)
    MainWindow.req_time = MainWindow.update_time
    lbl_time.config(text='Следующее обновление в ' + MainWindow.req_time)
    # schedule.every(MainWindow.update_minute).minutes.do(Update)
    print('up')
    # while True:
    #    schedule.run_pending()
    #    time.sleep(1)

if __name__ == '__main__':
    app = MainWindow()
    app.protocol("WM_DELETE_WINDOW", withdraw_window)
    app.mainloop()