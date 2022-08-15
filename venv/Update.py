import tkinter as tk
from PIL import Image
from pystray import MenuItem, Menu, Icon


def quit_window(icon, item):
    icon.stop()
    root.destroy()


def show_window(icon, item):
    icon.stop()
    root.after(0, root.deiconify)


def withdraw_window():
    root.withdraw()
    image = Image.open(r"C:\Users\vasta\PycharmProjects\Exchange_Rates\acc.ico")
    icon = Icon('main', image, 'Test', menu=Menu(MenuItem('Show', show_window), MenuItem('Quit', quit_window)))
    icon.run()


root = tk.Tk()
root.title('Test')
root.geometry('320x240')
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", withdraw_window)
root.mainloop()