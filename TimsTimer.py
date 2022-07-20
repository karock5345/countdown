#from re import T
from msilib.schema import ComboBox
import os
from tkinter import *
import datetime
import tkinter as tk
import icon
import base64

#import notify2 as notification
#from playsound import playsound


class Application(Frame):

    def __init__(self,master):
        super(Application, self).__init__(master)
        self.pack(anchor=CENTER,expand=1,fill=BOTH)
        self.createWidgets()
        self._alarm_id = None
        self._paused = False
        self._starttime = 25*60
        self._flash = False
        self._flash_on = False
        #self._alarm_id2 = self.master.after(1000, self.clocktimer)  
        self.master.after(1000, self.clocktimer)      
        self.setcustomtimer()
        

    def createWidgets(self): 
        # init count down : 1st=25:00, 2nd=00:20, 3rd=05:00      
        self.inticount = [2,5,0,0,0,0,2,0,0,5,0,0]
        self.var1min11 = IntVar()
        self.var1min1 = IntVar()
        self.var2min11 = IntVar()
        self.var2min1 = IntVar()
        self.var3min11 = IntVar()
        self.var3min1 = IntVar()

        self.var1sec11 = IntVar()
        self.var1sec1 = IntVar()
        self.var2sec11 = IntVar()
        self.var2sec1 = IntVar()
        self.var3sec11 = IntVar()
        self.var3sec1 = IntVar()

        list09 = [0,1,2,3,4,5,6,7,8,9]
        list05 = [0,1,2,3,4,5]
        
        self.timerVariable = StringVar()
        self.timerVariable.set('pomodoro')

        self.nowLabel = Label(self,text="----",font=("Tahoma",20),bg="red",fg="white", width="22")
        # self.timerLabel.grid(row=2,column=1)
        self.nowLabel.pack(side=TOP,pady="5")
        #e = datetime.datetime.now()
        #self.nowLabel.configure(text=e.strftime('%d/%m/%Y   %I:%M:%S %p'))    
        # print (e.strftime("%d/%m/%Y"))
        # print (e.strftime("%I:%M:%S %p"))

        
        self.optFrameG1 = Frame(self, bg="#2ba6cb")

        self.var1min11.set(list09[self.inticount[0]])
        self.opt1min11 = OptionMenu(self.optFrameG1,  self.var1min11, *list09, command=self.setcustomtimer)
        self.opt1min11.config(font=('Arial',12))
        self.opt1min11.pack(side=LEFT,padx='0')        

        self.var1min1.set(list09[self.inticount[1]])
        self.opt1min1 = OptionMenu(self.optFrameG1,  self.var1min1, *list09, command=self.setcustomtimer )
        self.opt1min1.config(font=('Arial',12))
        self.opt1min1.pack(side=LEFT,padx='0')

        self.var1sec11.set(list05[self.inticount[2]])
        self.opt1sec11 = OptionMenu(self.optFrameG1,  self.var1sec11, *list05, command=self.setcustomtimer )
        self.opt1sec11.config(font=('Arial',12))
        self.opt1sec11.pack(side=LEFT,padx='0')        

        self.var1sec1.set(list09[self.inticount[3]])
        self.opt1sec1 = OptionMenu(self.optFrameG1, self.var1sec1, *list09, command=self.setcustomtimer )
        self.opt1sec1.config(font=('Arial',12))
        self.opt1sec1.pack(side=LEFT,padx='0')

        
        self.g1Button = Radiobutton(self.optFrameG1,text="Pomodoro",width="8",bg="#2ba6cb",variable=self.timerVariable,selectcolor="#2284a1",value="pomodoro",activebackground="#2284a1",height='2',font=('Arial',16),indicatoron=0,command=self.startClock)
        self.g1Button.pack(side=LEFT,padx='0')

        self.optFrameG1.pack(side=TOP)


        self.optFrameG2 = Frame(self, bg="#2ba6cb")
        self.var2min11.set(list09[self.inticount[4]])
        self.opt2min11 = OptionMenu(self.optFrameG2,  self.var2min11, *list09, command=self.setcustomtimer )
        self.opt2min11.config(font=('Arial',12))
        self.opt2min11.pack(side=LEFT,padx='0')        

        self.var2min1.set(list09[self.inticount[5]])
        self.opt2min1 = OptionMenu(self.optFrameG2,  self.var2min1, *list09, command=self.setcustomtimer )
        self.opt2min1.config(font=('Arial',12))
        self.opt2min1.pack(side=LEFT,padx='0')

        self.var2sec11.set(list05[self.inticount[6]])
        self.opt2sec11 = OptionMenu(self.optFrameG2,  self.var2sec11, *list05, command=self.setcustomtimer)
        self.opt2sec11.config(font=('Arial',12))
        self.opt2sec11.pack(side=LEFT,padx='0')        

        self.var2sec1.set(list09[self.inticount[7]])
        self.opt2sec1 = OptionMenu(self.optFrameG2,  self.var2sec1, *list09 , command=self.setcustomtimer)
        self.opt2sec1.config(font=('Arial',12))
        self.opt2sec1.pack(side=LEFT,padx='0')

        self.g2Button = Radiobutton(self.optFrameG2,text="Pomodoro",width="8",bg="#2ba6cb",variable=self.timerVariable,selectcolor="#2284a1",value="short break",activebackground="#2284a1",height='2',font=('Arial',16),indicatoron=0,command=self.startClock)
        self.g2Button.pack(side=LEFT,padx='0')

        self.optFrameG2.pack(side=TOP)









        self.optFrameG3 = Frame(self, bg="#2ba6cb")


        self.var3min11.set(list09[self.inticount[8]])
        self.opt3min11 = OptionMenu(self.optFrameG3,  self.var3min11, *list09, command=self.setcustomtimer )
        self.opt3min11.config(font=('Arial',12))
        self.opt3min11.pack(side=LEFT,padx='0')        

        self.var3min1.set(list09[self.inticount[9]])
        self.opt3min1 = OptionMenu(self.optFrameG3,  self.var3min1, *list09 , command=self.setcustomtimer)
        self.opt3min1.config(font=('Arial',12))
        self.opt3min1.pack(side=LEFT,padx='0')

        self.var3sec11.set(list05[self.inticount[10]])
        self.opt3sec11 = OptionMenu(self.optFrameG3,  self.var3sec11, *list05, command=self.setcustomtimer )
        self.opt3sec11.config(font=('Arial',12))
        self.opt3sec11.pack(side=LEFT,padx='0')        

        self.var3sec1.set(list09[self.inticount[11]])
        self.opt3sec1 = OptionMenu(self.optFrameG3,  self.var3sec1, *list09, command=self.setcustomtimer )
        self.opt3sec1.config(font=('Arial',12))
        self.opt3sec1.pack(side=LEFT,padx='0')

        self.g3Button = Radiobutton(self.optFrameG3,text="long",width="8",bg="#2ba6cb",variable=self.timerVariable,selectcolor="#2284a1",value="long break",activebackground="#2284a1",height='2',font=('Arial',16),indicatoron=0,command=self.startClock)
        self.g3Button.pack(side=LEFT,padx='0')
        self.optFrameG3.pack(side=TOP)

        # self.radioFrame = Frame(self,bg="#2ba6cb")
        # self.pomodoroButton = Radiobutton(self.radioFrame,text="Pomodoro",width="15",bg="#2ba6cb",variable=self.timerVariable,selectcolor="#2284a1",value="pomodoro",activebackground="#2284a1",height='2',font=('Arial',9),indicatoron=0,command=self.startClock)
        # self.pomodoroButton.pack(side=LEFT,padx='0')

        # self.shortBreakButton = Radiobutton(self.radioFrame,text="20 sec.",width="15",bg="#2ba6cb",variable=self.timerVariable,selectcolor="#2284a1",value="short break",activebackground="#2284a1",height='2',font=('Arial',9),indicatoron=0,command=self.startClock)
        # self.shortBreakButton.pack(side=LEFT,padx='0')

        # self.longBreakButton = Radiobutton(self.radioFrame,text="5 min.",width="15",bg="#2ba6cb",variable=self.timerVariable,selectcolor="#2284a1",value="long break",activebackground="#2284a1",height='2',font=('Arial',9),indicatoron=0,command=self.startClock)
        # self.longBreakButton.pack(side=LEFT,padx='0')

        # self.radioFrame.pack(side=TOP)


        #self.timerLabel = Label(self,text="25:00",font=("Cantrell",70),bg="red",fg="white")
        self.timerLabel = Label(self,text="--:--",font=("Monospac821 BT",70),bg="red",fg="white")
        
        # self.timerLabel.grid(row=2,column=1)
        self.timerLabel.pack(side=TOP,pady="5")

        self.secondButtonFrame = Frame(self,bg="white")
        self.startButton = Button(self.secondButtonFrame,text="Start",fg="white",bg="#5da423",activebackground="green",activeforeground="white",width="8",height="2",font=('Arial',11),command=self.startTime)
        # self.startButton.grid(row=3,column=0,sticky=W)
        self.startButton.pack(side=LEFT,padx='5')

        self.stopButton = Button(self.secondButtonFrame,text="Stop",fg="white",bg="red",width="8",height="2",activebackground="#c60f13",activeforeground="white",font=('Arial',11),command=self.stopTime)
        # self.stopButton.grid(row=3,column=1,sticky=NSEW)
        self.stopButton.pack(side=LEFT,padx='5')

        self.resetButton = Button(self.secondButtonFrame,text="Reset",fg="black",width="8",height="2",font=('Arial',11),command=self.resetTime)
        # self.resetButton.grid(row=3,column=2,sticky=E)
        self.resetButton.pack(side=LEFT,padx='5')
        self.secondButtonFrame.pack(side=TOP,pady="5")


    def startClock(self):
        self.changetimer()
        if self._alarm_id is not None:
            self.master.after_cancel(self._alarm_id)
        self._paused = False
        self.countdown(self._starttime)
        


    def startTime(self):
        self._paused = False
        if self._alarm_id is None:
            self.countdown(self._starttime)

    def stopTime(self):
        if self._alarm_id is not None:
            self._paused = True

    # I have to work on the reset method more cos it's not working as I expect
    def resetTime(self):
        
        self.master.after_cancel(self._alarm_id)
        self._alarm_id = None
        self._paused = False
        self.countdown(self._starttime)
        self._paused = True
    def clocktimer(self):
        e = datetime.datetime.now()
        self.nowLabel.configure(text=e.strftime('%#d/%#m/%Y %a %#I:%M%p'))  
        # windows use %#S, linux use %-S  
        #self.nowLabel.configure(text=e.strftime('%#S')) 
        # self.nowLabel.configure(text=e.strftime('%d/%m/%Y   %I:%M:%S %p'))  
        #self.nowLabel.configure(text=e.strftime('23/45/2022 Sun 23:50PM'))      
        self.master.after(1000, self.clocktimer)

    def countdown(self,timeInSeconds, start=True):
        if timeInSeconds >= 0:
            self._flash = False
            self._flash_on = False
            if start:
                self._starttime = timeInSeconds
            if self._paused:
                self._alarm_id = self.master.after(1000,self.countdown,timeInSeconds,False)
            else:
                mins,secs = divmod(timeInSeconds,60)
                timeformat = "{0:02d}:{1:02d}".format(mins,secs)
                app.timerLabel.configure(text=timeformat)
                self._alarm_id = self.master.after(1000,self.countdown,timeInSeconds-1,False)
        else:
            #notification.init('Pomodoro Timer')
            #notification.Notification("Time up!!!!").show()
            print('Time up!!!!\a')
            self._flash = True
            self._alarm_id = self.master.after(500, self.flashtimer)
            # playsound('../Alarm/bellring.wav')

    def flashtimer(self):
        if self._flash == True :
            if self._flash_on == False :
                app.timerLabel.configure(text='     ')                
                self._flash_on = True
            else:
                app.timerLabel.configure(text='00:00')
                self._flash_on = False
            self._alarm_id = self.master.after(500, self.flashtimer)

    def setcustomtimer(self, *args):
        self.g1Button.configure(text=str(self.var1min11.get()) + str(self.var1min1.get())  + ':' + str(self.var1sec11.get()) + str(self.var1sec1.get()))
        self.g2Button.configure(text=str(self.var2min11.get()) + str(self.var2min1.get())  + ':' + str(self.var2sec11.get()) + str(self.var2sec1.get()))
        self.g3Button.configure(text=str(self.var3min11.get()) + str(self.var3min1.get())  + ':' + str(self.var3sec11.get()) + str(self.var3sec1.get()))
        self.changetimer()
    def changetimer(self):
        timerToStart = self.timerVariable.get()
        if timerToStart == "pomodoro":
            min = self.var1min11.get() * 10 + self.var1min1.get()
            sec = self.var1sec11.get() * 10 + self.var1sec1.get()
        elif timerToStart == "short break":
            min = self.var2min11.get() * 10 + self.var2min1.get()
            sec = self.var2sec11.get() * 10 + self.var2sec1.get()
        elif timerToStart == "long break":
            min = self.var3min11.get() * 10 + self.var3min1.get()
            sec = self.var3sec11.get() * 10 + self.var3sec1.get()
        self._starttime = min * 60 + sec

if __name__ == '__main__':
    root = Tk()
    #root.iconbitmap(r"C:\Users\Tim\Documents\Projects\Python examples\CountDown\clock.ico")
    #root.iconbitmap(r".\\clock.ico")
    with open('tmp.ico','wb') as tmp:
        tmp.write(base64.b64decode(icon.Icon().img))
    root.iconbitmap('tmp.ico')
    os.remove('tmp.ico')    
    
    
    
    root.title("Tim Wong's Timer")
    root.resizable(0,0)
    app = Application(root)
    app.configure(background="white")

    root.mainloop()