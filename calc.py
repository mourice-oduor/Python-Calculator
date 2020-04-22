from tkinter import *
import tkinter as tk
import os
import re #(Regular expression)

class Calculator:
    def __init__(self, cal):
        self.cal = cal
        cal.title('Simple Python Calculator')
        #cal.iconbitmap(r'/home/net/MORYSO/PYTHON/Game-Dev/games-todo/16. Calculator/calculator.icon')
        #cal.iconbitmap('calculator.icon')
        dark_grey = '#141414'
        med_grey = '#212121'
        cus_red = '#c41212'
        self.screen = Text(cal, background=dark_grey, font=('Helvetica', 32), height=1, state='disabled',
                           foreground='white', bd=0, pady=50, padx=5, selectbackground=dark_grey, inactiveselectbackground=dark_grey)

        for x in range(1,5):
            self.cal.columnconfigure(x, weight=1)
            self.cal.rowconfigure(x, weight=1)

        self.screen.grid(row=0, column=0, columnspan=5, sticky=W+E+N+S)
        self.screen.configure(state='normal')
        self.equation = ''
        self.cal.geometry('500x600') #Default size to open into
        btn1 =  self.createButton(7)
        btn2 = self.createButton(8)
        btn3 = self.createButton(9)
        btn4 = self.createButton(u"\u00F7", bg=med_grey)
        btn5 = self.createButton(4)
        btn6 = self.createButton(5)
        btn7 = self.createButton(6)
        btn8 = self.createButton(u"\u00D7", bg=med_grey)
        btn9 = self.createButton(1)
        btn10 = self.createButton(2)
        btn11 = self.createButton(3)
        btn12 = self.createButton('-', bg=med_grey)
        btn13 = self.createButton(',')
        btn14 = self.createButton(0)
        btn15 = self.createButton(None)
        btn16 = self.createButton('+', bg=med_grey)
        btn17 = self.createButton('DEL', None, bg=med_grey)
        btn18 = self.createButton('CLR', None, bg=med_grey)
        btn19 = self.createButton('=', None, bg=cus_red)
        btn15.config(state='disabled')
        buttons = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn13,btn14,btn15,btn16,btn17,btn18,btn19]

        count = 0

        for row in range(1,5):
            for col in range(4):
                buttons[count].grid(row=row, column=col,sticky=W+E+N+S)
                count+=1
        buttons[16].grid(row=1, column=4, rowspan=1, sticky=W+E+N+S)
        buttons[17].grid(row=2, column=4, rowspan=2, sticky=W+E+N+S)
        buttons[18].grid(row=4, column=4, rowspan=1, sticky=W+E+N+S)

    def createButton(self, val, write=True, width=5, bg='black'):
        return Button(self.cal, text=val, command=lambda:self.click(val, write), width=width, bg=bg, bd=0, fg='white',
                      font=('Helvetica',24))

    def click(self, text, write):
        if write == None:
            if text == '=' and self.equation:
                self.equation = re.sub(u'\u00F7', '/', self.equation)
                self.equation = re.sub(u'\u00D7', '*', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer,newline=True)
            elif text == "CLR":
                self.clear_screen()
            elif text == 'DEL':
                self.del_screen()
        else:
            # add text to screen
            self.insert_screen(text)


    def clear_screen(self):
        #to clear screen
        #set equation to empty before deleting screen
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete(1.0, END)
        self.screen.configure(state='disabled')

    def del_screen(self):
        #to clear screen
        #set equation to empty before deleting screen
        self.equation = self.equation[:-1]
        self.screen.configure(state='normal')
        text = self.screen.get("1.0",END)[:-2]
        self.screen.tag_config('val',justify=RIGHT)
        self.screen.delete(1.0, END)
        self.screen.insert(END,text, 'val')
        self.screen.configure(state='disabled')

    def insert_screen(self, value,newline=False):
        self.screen.configure(state='normal')
        self.screen.tag_config('val',justify=RIGHT)
        self.screen.insert(END,str(value),'val')
        # record every value inserted in screen
        self.equation += str(value)
        self.screen.configure(state ='disabled')

calc = Tk()
my_gui = Calculator(calc)
calc.mainloop()
if __name__ == '__main__':
    print('My Calculator')
