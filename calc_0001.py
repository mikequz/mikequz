import math
from decimal import *
from tkinter import *

class Calculator:
    res=''
    def __init__(self, window, oper='', op1='', op2=''):
        self.oper=oper
        self.op1=op1
        self.op2=op2
        self.window=window
        self.initUI(self.window)  
        
    def calc(self):
        """Вычисляет простые операции +, -, *, /, sqrt"""
        self.res=0
        getcontext().prec = 10 #устанавливаем точность для модуля decimal

        if self.op1 == '': #если = нажато без чисел оставляем 0
            self.op1 = '0'
        elif self.op2 == '':
            self.op2 = self.op1 #реализуем операцию (+,-,*,/) числа на себя

        if self.oper == '+':
            self.res = math.fsum([float(self.op1), float(self.op2)])
        elif self.oper == '-':
            self.res = float(self.op1) - float(self.op2)
        elif self.oper == 'x':
            self.res = Decimal(float(self.op1)) * Decimal(float(self.op2))
        elif self.oper == chr(247):
            try:
                self.res = float(self.op1) / float(self.op2)
            except ZeroDivisionError:
                self.res = 'Ошибка: деление на ноль'
        elif self.oper == 'sqrt':
            self.res = math.sqrt(float(self.op1))
        elif '%' in self.lbl2.cget('text'):
            pass

        self.remove()
        self.lbl.configure(text=self.res)
        self.lbl2.configure(text=(self.op1 + ' ' + self.oper
                                  + ' ' + self.op2 + ' ='))
        self.output()
        self.op1 = self.res     #после вывода результата он становится первым 
        self.op2 = ''      #оператором и можно продолжать вычисления
        self.oper = ''

    def perc(self):
        """Вычисляет процент"""
        self.res = ''
        if self.oper == '+':
            self.res = float(self.op1) + float(self.op1) * float(self.op2) / 100
        elif self.oper == '-':
            self.res = float(self.op1) - float(self.op1) * float(self.op2) / 100
        elif self.oper == 'x':
            self.res = float(self.op1) * float(self.op2) /100
        elif self.oper == chr(247):
            self.res = float(self.op1) / float(self.op2) * 100

        self.remove()
        self.lbl.configure(text=self.res)
        self.lbl2.configure(text=(self.op1 + ' ' + self.oper
                                    + ' ' + self.op2 + '% ='))
        self.output()
        self.op1 = self.res     #после вывода результата он становится первым оператором
        self.op2 = ''        #и можно продолжать вычисления
        self.oper = ''

    def remove(self):
        """Удаляет нули после запятой"""
        self.res = str(self.res)    #убираем ноль после запятой
        if self.res =='0.0':
            self.res = '0'
        elif '.' in self.res:
            for i in range(len(self.res)-1, -1, -1): 
                if self.res[i] == '0':  
                    self.res = self.res[0:i]
                else: break
            if self.res[-1] == '.':
                self.res = self.res[0:-1]
        return self.res
                
    def btnPush(self, opertmp):
        if self.oper != '': #реализуем выполнение предыдущей операции 
            self.calc()     #при нажатии +, -, *, /, sqrt вместо =
        self.oper=opertmp
        if self.op1 == '':
            self.op1 = '0'
        self.lbl2.configure(text=(self.op1, self.oper))

    def dig(self, dgt):
        """Выводит число в Label"""
        if dgt == '.' and '.' in self.lbl.cget('text'): #проверяем наличие точки во вводе
                pass
        else:
            if self.oper =='':
                if self.op1 =='0':  #реализум отображение для случая op1==0
                    self.op1 = ''
                if dgt == '.' and self.op1 == '': #добавляем 0, если ввод начат с '.'
                    self.op1= '0'
                self.op1 += dgt
                self.lbl.configure(text=self.op1)
            else:
                if dgt == '.' and self.op2 == '':#добавляем 0, если ввод начат с '.'
                    self.op2= '0'
                self.op2 += dgt
                self.lbl.configure(text=self.op2)
        self.lbl2.configure(text=(self.op1 + ' ' +
                                          self.oper + ' ' + self.op2))
        self.output()

    def output(self):
        """Изменяет размер щрифта в зависимости от длины содержимого Label"""
        if 10 < len(self.lbl.cget('text')) <= 15:
            self.lbl.configure(height = 1, font=('tahoma', 25))
        elif 16 <= len(self.lbl.cget('text')) <= 25:
            self.lbl.configure(font=('tahoma', 15))
        elif 26 <= len(self.lbl.cget('text')):
            self.lbl.configure(font=('tahoma', 10))
            self.lbl2.configure(font=('tahoma', 10))
        else:
            self.lbl.configure(font=('tahoma', 40))
            self.lbl2.configure(font=('tahoma', 15))
                
    def back(self):
        """Стирает последний символ в Label"""
        try:
            if self.oper =='':
                self.op1 = self.op1[0:len(self.op1)-1]
                if self.op1 =='':
                        self.lbl.configure(text='0')
                else:
                        self.lbl.configure(text=self.op1)
            else:
                self.op2 = self.op2[0:len(self.op2)-1]
                if self.op2 == '':
                        self.lbl.configure(text='0')
                else:
                        self.lbl.configure(text=self.op2)
        except IndexError: pass
        self.lbl2.configure(text=(self.op1 + ' ' + self.oper + ' ' + self.op2))
        self.output()

    def clr(self):
        """Очищает значения и поля"""
        self.oper =''
        self.op1 =''
        self.op2=''
        self.lbl.configure(text='0', font=('tahoma', 40))
        self.lbl2.configure(text='')

    def initUI(self, window):
        """Инициализирует интерфейс"""
        self.window.geometry('300x421')
        self.window.title('Calculator')
        self.frame1=Frame(self.window)
        self.frame2=Frame(self.window)
        self.frame3=Frame(self.window, height=20, width=296)#,
                          #borderwidth=1, relief='solid')
        self.frame1.pack(anchor='ne')
        self.frame3.pack(fill=None, expand=False, anchor='ne')
        self.frame2.pack(anchor='s')
        self.lbl = Label(self.frame3, text='0', font=('tahoma', 40), fg='dark blue')
        self.lbl2 = Label(self.frame1, font=('tahoma', 15))
        self.lbl2.pack(anchor='ne')
        self.lbl.pack(anchor='ne')

        btn1=Button(self.frame2, text='1', bd=1, command=lambda: self.dig('1'),
                                   font=('tahoma', 15),  width=6, height=2, relief='flat')
        btn2=Button(self.frame2, text='2', bd=1, command=lambda: self.dig('2'),
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        btn3=Button(self.frame2, text='3', bd=1, command=lambda: self.dig('3'),
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        btn4=Button(self.frame2, text='4', bd=1, command=lambda: self.dig('4'),
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        btn5=Button(self.frame2, text='5', bd=1, command=lambda: self.dig('5'),
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        btn6=Button(self.frame2, text='6', bd=1, command=lambda: self.dig('6'),
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        btn7=Button(self.frame2, text='7', bd=1, command=lambda: self.dig('7'),
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        btn8=Button(self.frame2, text='8', bd=1, command=lambda: self.dig('8'),
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        btn9=Button(self.frame2, text='9', bd=1, command=lambda: self.dig('9'),
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        btn0=Button(self.frame2, text='0', bd=1, command=lambda: self.dig('0'),
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        btn_dot=Button(self.frame2, text='.', bd=1, command=lambda: self.dig('.'),
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        
        btn_plus=Button(self.frame2, text='+', bd=1, command=lambda: self.btnPush('+'),
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        btn_minus=Button(self.frame2, text='-', bd=1, command=lambda: self.btnPush('-'),
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        btn_mult=Button(self.frame2, text='x', bd=1, command=lambda: self.btnPush('x'),
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        btn_divide=Button(self.frame2, text=chr(247), bd=1, command=lambda: self.btnPush(chr(247)),
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        btn_sqrt=Button(self.frame2, text='sqr', bd=1, command=lambda: self.btnPush('sqrt'),
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        btn_perc=Button(self.frame2, text='%', bd=1, command=self.perc,
                                    font=('tahoma', 15), width=6, height=2, relief='flat')

        btn_equa=Button(self.frame2, text='=', bd=1, command=self.calc,
                                    font=('tahoma', 15), width=6, height=2, bg='light blue', relief='flat')
        btn_clr=Button(self.frame2, text='C', bd=1, command=self.clr,
                                    font=('tahoma', 15), width=6, height=2, relief='flat')
        btn_back=Button(self.frame2, text=chr(9003), bd=1, command=self.back,
                                    font=('tahoma', 15), width=6, height=2, relief='flat')

        btn1.grid(column=0, row=4)
        btn2.grid(column=1, row=4)
        btn3.grid(column=2, row=4)
        btn4.grid(column=0, row=3)
        btn5.grid(column=1, row=3)
        btn6.grid(column=2, row=3)
        btn7.grid(column=0, row=2)
        btn8.grid(column=1, row=2)
        btn9.grid(column=2, row=2)
        btn0.grid(column=1, row=5)
        btn_dot.grid(column=0, row=5)
        
        btn_plus.grid(column=3, row=1)
        btn_minus.grid(column=3, row=2)
        btn_mult.grid(column=3, row=3)
        btn_divide.grid(column=3, row=4)
        btn_sqrt.grid(column=2, row=1)
        btn_perc.grid(column=2, row=5)
        
        btn_equa.grid(column=3, row=5)
        btn_back.grid(column=1, row=1)
        btn_clr.grid(column=0, row=1)
        
        
if __name__=='__main__':
    root = Tk()
    App=Calculator(root)
    root.mainloop()
