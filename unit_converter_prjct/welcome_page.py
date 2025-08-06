import tkinter as tk
from tkinter.ttk import Progressbar
from time import sleep

class WelcomePage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg='#b0c1b1')
        self.root.title("Unit Converter")
        self.root.geometry("500x300")

        intro = tk.Label(self.root, bg='#b0c1b1', fg="brown", text="Welcome to Unit Converter", font=("Courier", 20, "bold"))
        intro.place(x=50, y=30, width=400, height=30)

        self.load = Progressbar(self.root, orient="horizontal", length=250, mode='indeterminate')
        self.start = tk.Button(self.root, bg='#f5f5f5', fg="brown", text="START", command=self.loading)
        self.start.place(x=200, y=90, width=80, height=30)


        self.root.mainloop()
    
    def loading(self):
        self.start.place(x=0,y=0,width=0, height=0)
        self.load.place(x=120, y=100)
        self.root.update()

        self.load['value'] = 20
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 40
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 50
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 60
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 80
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 100
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 80
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 60
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 50
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 40
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 20
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 0
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 20
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 40
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 50
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 60
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 80
        self.root.update_idletasks()
        sleep(0.2)

        self.load['value'] = 100
        self.root.update_idletasks()
        sleep(0.2)