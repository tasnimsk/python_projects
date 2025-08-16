import tkinter as tk
from tkinter.ttk import Progressbar
from time import sleep
from tkinter import END
import os

class Converter:
    def __init__(self, unit):
        self.root = tk.Tk()
        self.root.configure(bg='#b0c1b1')
        self.root.title("Unit Converter")
        self.root.geometry("500x500")

        self.unit = unit

        upr = tk.Label(self.root, bg='#add8e6', width=400, height=250)
        upr.place(x=0,y=0)

        lwr = tk.Label(self.root, bg="#80b8c3", width=400, height=250,bd=0)
        lwr.place(x=0,y=250)


        self.menu_lb = tk.Listbox(self.root, selectmode="single", height=0, font=("Helvetica", 10))
        self.menu_lb.bind('<<ListboxSelect>>', self.set_unit)

        options = ["", "", "Length", "Temperature", "Speed", "Time", "Mass"]
        for i in range(len(options)):
            self.menu_lb.insert(i, options[i])

        self.pic= tk.PhotoImage(file=r"C:\Users\moath\Downloads\python_projects\unit_converter_prjct\menu.png")
        self.menu= tk.Button(self.root,image=self.pic,width=35,height=30,bg="#add8e6",bd=0,command=lambda:self.select('m'))
        self.menu.place(x=0,y=0)

        self.inp_stg = tk.StringVar()
        self.inp = tk.Entry(self.root, bg='#add8e6', fg="white", font=("Helvetica", 14), textvariable=self.inp_stg, bd=1)
        self.inp.place(x=120, y=100, width=116, height=40)
        self.inp.bind('<KeyRelease>', self.operation)
        self.inp.bind('<BackSpace>', self.operation)

        self.lb_menu = unit["lb"]


        self.lb = tk.Listbox(self.root, selectmode="single", height=0)
        self.lb.bind('<<ListboxSelect>>', self.set_unit)

        self.disp = tk.Label(self.root, text= self.lb_menu[0], bg="white", fg="black")
        self.disp.place(x=120,y=160,width=100,height=20)

        self.down= tk.PhotoImage(file=r"C:\Users\moath\Downloads\python_projects\unit_converter_prjct\down.png")
        scroll_upr= tk.Button(self.root,image=self.down,width=14,height=18,bd=0,command=lambda:self.select(0))
        scroll_upr.place(x=220,y=160)

        self.opt_stg = tk.StringVar()
        self.opt = tk.Entry(self.root, bg='#189ab4', fg="black", font=("Helvetica", 14), textvariable= self.opt_stg, bd=1)
        self.opt.place(x=120, y=350,width=116,height=40)
        self.opt.bind('<KeyRelease>', self.operation)

        self.lb1 = tk.Listbox(self.root, selectmode="single", height=0)
        self.lb1.bind('<<ListboxSelect>>', self.set_unit)

        for i in range(len(self.lb_menu)):
            self.lb1.insert(i, self.lb_menu[i]) #used END where i is
            self.lb.insert(i, self.lb_menu[i]) # ^
        
        self.disp1 = tk.Label(self.root, text= self.lb_menu[1], bg='#ffffff', fg="black")
        self.disp1.place(x=120,y=410,width=100,height=20)

        scroll_dwn= tk.Button(self.root,image=self.down,width=14,height=18,bd=0,command=lambda:self.select(1),bg="#f5f5f5")
        scroll_dwn.place(x=220,y=410)

        self.form = tk.StringVar()
        self.formulae = tk.Label(self.root, text="", bg='#189ab4', fg="white", font=("Helvetica", 10))
        self.formulae.place(x=50, y=450, width=250, height=25)

        self.para = unit["para"]
        self.para1 = unit["para1"]

        self.root.mainloop()
    
    def select(self, option):
        if option == 'm':
            print("Menu button clicked")
            if self.menu_lb.winfo_ismapped():
                self.menu_lb.place_forget()
            else:
                self.menu_lb.place(x=50, y=30, width=100, height=150)

        elif option == 0:
            print("Upper scroll button clicked")
            self.lb.yview_scroll(-1, "units")

        elif option == 1:
            print("Lower scroll button clicked")
            self.lb1.yview_scroll(1, "units")

        self.root.update()
    
    def set_unit(self, event):
        global exp_in, exp_out
        exp_in = ""
        exp_out = ""

        self.inp_stg.set("")
        self.opt_stg.set("")

        widget = event.widget
        selection = widget.curselection()

        if selection:
            index = selection[0]
            unit = widget.get(index)
            self.unit = unit

            self.lb_menu = unit["lb"]
            self.lb.delete(0,END)
            self.lb1.delete(0, END)
            self.lb.place(y=0, height=0)
            self.lb1.place(y=250, height=0)
#   
            self.disp['text'] = self.lb_menu[0]
            self.disp1['text'] = self.lb_menu[1]
#   
            self.para = unit["para"]
            self.para1 = unit["para1"]

        for i in range(len(self.lb_menu)):
            self.lb1.insert(END, self.lb_menu[i])
            self.lb.insert(i, self.lb_menu[i])
        
        self.formulae['text'] = "Formulae: " + operator.replace("{}", "Unit")

        self.root.update()

    def operation(self, event):
        global exp_in, exp_out, operator
        self.inp_unit = self.disp['text']
        self.opt_unit = self.disp1['text']

        try:
            widget = event.widget
            if widget == self.inp:
                self.root.update()
                index = self.unit[self.opt_unit][-1]
                operator = self.unit[self.inp_unit][index]

                if event.char and event.char >= '0' and event.char <= '9':
                    exp_in = self.inp_stg.get()
                    exp_out = str(eval(operator.format(exp_in)))
                    self.opt_stg.set(exp_out)
                
                elif event.keysym == 'BackSpace' or (len(self.inp_stg.get()) == 0 and event.char and event.char.isdigit()):
                    exp_out = self.opt_stg.get()
                    operator = self.unit[self.opt_unit][self.unit[self.inp_unit][-1]]
                    exp_in = str(eval(operator.format(exp_out)))
                    self.inp_stg.set(exp_in)
        except Exception as e:
            print(f"Error: {e}")