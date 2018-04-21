from tkinter import *
import time
mywin=Tk()
ment=StringVar()


class app(Frame):
    
    def __init__(self,master):

        Frame.__init__(self,master)
        self.master=master
        self.option_add('*font','arial 20 bold')
        self.pack(expand=YES,fill=BOTH)
        self.master.title('Calculator')
        self.next()
        
    def next(self):
       

        self.display=Entry(self,textvariable=ment,justify='left',bg='powder blue')
        self.display.place(x=0,y=0)

    
        button1=Button(self,padx=10,pady=10,text='1',command=self.one)
        button1.place(x=0,y=35)
       
        button2=Button(self,padx=10,pady=10,text='2',command=self.two)
        button2.place(x=60,y=35)
        
        button3=Button(self,padx=10,pady=10,text='3',command=self.tree)
        button3.place(x=120,y=35)
       
        button4=Button(self,padx=10,pady=10,text='4',command=self.four)
        button4.place(x=0,y=105)
        
        button5=Button(self,padx=10,pady=10,text='5',command=self.five)
        button5.place(x=60,y=105)
        
        button6=Button(self,padx=10,pady=10,text='6',command=self.six)
        button6.place(x=120,y=105)
        
        button7=Button(self,padx=10,pady=10,text='7',command=self.seven)
        button7.place(x=0,y=175)
        
        button8=Button(self,padx=10,pady=10,text='8',command=self.eit)
        button8.place(x=60,y=175)
        
        button9=Button(self,padx=10,pady=10,text='9',command=self.nine)
        button9.place(x=120,y=175)

        buttonPlus=Button(self,padx=9,pady=10,text='+',command=self.plus)
        buttonPlus.place(x=180,y=35)

        buttonMinus=Button(self,padx=12,pady=10,text='-',command=self.minus)
        buttonMinus.place(x=180,y=105)

        buttonMut=Button(self,padx=11,pady=10,text='*',command=self.mut)
        buttonMut.place(x=180,y=175)

        buttonDev=Button(self,padx=13,pady=10,text='/',command=self.dev)
        buttonDev.place(x=180,y=245)

        buttonHav=Button(self,padx=9.5,pady=10,text='=',command=self.hav)
        buttonHav.place(x=120,y=245)

        button0=Button(self,padx=10,pady=10,text='0',command=self.zero)
        button0.place(x=60,y=245)

        buttonC=Button(self,padx=10,pady=10,text='c',command=self.C)
        buttonC.place(x=0,y=245)

        buttonPow=Button(self,padx=10,pady=10,text='^',command=self.pow)
        buttonPow.place(x=240,y=35)

        buttonPoint=Button(self,padx=12,pady=10,text='.',command=self.point)
        buttonPoint.place(x=240,y=105)

        buttonBacP=Button(self,padx=10,pady=10,text='(',command=self.bacp)
        buttonBacP.place(x=240,y=175)

        buttonPakP=Button(self,padx=10,pady=10,text=')',command=self.pakp)
        buttonPakP.place(x=240,y=245)

        

    def one(self):
        
        global layn
        inpText=self.display.get()
        layn=(len(inpText)+1)
        
        self.display.insert(layn,'1')
        
    def two(self):
        inpText=self.display.get()
        layn=(len(inpText)+1)
        self.display.insert(layn,'2')
    def esh():
        print('hello')
        
    def tree(self):
        inpText=self.display.get()
        layn=(len(inpText)+1)
        self.display.insert(layn,'3')

    def four(self):
        inpText=self.display.get()
        layn=(len(inpText)+1)
        self.display.insert(layn,'4')

    def five(self):
        
        inpText=self.display.get()
        layn=(len(inpText)+1)
        self.display.insert(layn,'5')
        
    def six(self):
        
        inpText=self.display.get()
        layn=(len(inpText)+1)
        self.display.insert(layn,'6')
        
    def seven(self):
        inpText=self.display.get()
        layn=(len(inpText)+1)
        self.display.insert(layn,'7')

    def eit(self):
        inpText=self.display.get()
        layn=(len(inpText)+1)
        self.display.insert(layn,'8')

    def nine(self):
        inpText=self.display.get()
        layn=(len(inpText)+1)
        self.display.insert(layn,'9')

    def plus(self):
        self.display.insert(END,'+')

    def minus(self):
        self.display.insert(END,'-')

    def mut(self):
        self.display.insert(END,'*')

    def dev(self):
        self.display.insert(END,'/')

    def hav(self):
        
        
        try:
            inpText=self.display.get()
            number=eval(inpText)
            self.display.insert(END,'=')
            self.display.insert(END,number)
        except: 
            self.display.delete(0,END)
            self.display.insert(END,'ERROR')


           

        

        
    
    def C(self):
        self.display.delete(0,END)

    def zero(self):
        self.display.insert(END,'0')

    def pow(self):
        self.display.insert(END,'**')

    def point(self):
        self.display.insert(END,'.')

    def bacp(self):
         self.display.insert(END,'(')

    def pakp(self):
         self.display.insert(END,')')
                


mywin.geometry('288x320')
mywin.resizable(0, 0)       
appd=app(mywin)
mywin.mainloop()


