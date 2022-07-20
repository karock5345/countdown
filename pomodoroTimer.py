from re import T
from tkinter import *
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

    def createWidgets(self):

        self.timerVariable = StringVar()
        self.timerVariable.set(None)

        self.firstButtonFrame = Frame(self,bg="#2ba6cb")
        self.pomodoroButton = Radiobutton(self.firstButtonFrame,text="Pomodoro",width="15",bg="#2ba6cb",variable=self.timerVariable,selectcolor="#2284a1",value="pomodoro",activebackground="#2284a1",height='2',font=('Arial',9),indicatoron=0,command=self.startClock)
        self.pomodoroButton.pack(side=LEFT,padx='0')

        self.shortBreakButton = Radiobutton(self.firstButtonFrame,text="20 sec.",width="15",bg="#2ba6cb",variable=self.timerVariable,selectcolor="#2284a1",value="short break",activebackground="#2284a1",height='2',font=('Arial',9),indicatoron=0,command=self.startClock)
        self.shortBreakButton.pack(side=LEFT,padx='0')

        self.longBreakButton = Radiobutton(self.firstButtonFrame,text="5 min.",width="15",bg="#2ba6cb",variable=self.timerVariable,selectcolor="#2284a1",value="long break",activebackground="#2284a1",height='2',font=('Arial',9),indicatoron=0,command=self.startClock)
        self.longBreakButton.pack(side=LEFT,padx='0')

        self.firstButtonFrame.pack(side=TOP)


        #self.timerLabel = Label(self,text="25:00",font=("Cantrell",70),bg="red",fg="white")
        self.timerLabel = Label(self,text="25:00",font=("Monospac821 BT",70),bg="red",fg="white")
        
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
        timerToStart = self.timerVariable.get()
        if timerToStart == "pomodoro":
            if self._alarm_id is not None:
                self.master.after_cancel(self._alarm_id)
            self._paused = False
            self.countdown(1500)



        elif timerToStart == "short break":
            if self._alarm_id is not None:
                self.master.after_cancel(self._alarm_id)
            self._paused = False
            self.countdown(20)


        elif timerToStart == "long break":
            if self._alarm_id is not None:
                self.master.after_cancel(self._alarm_id)
            self._paused = False
            self.countdown(300)


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

    def countdown(self,timeInSeconds, start=True):
        if timeInSeconds >= 0:
            self._flash = False
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
                app.timerLabel.configure(text='00:00')                
                self._flash_on = True
            else:
                app.timerLabel.configure(text='     ')
                self._flash_on = False
            self._alarm_id = self.master.after(500, self.flashtimer)



if __name__ == '__main__':
    root = Tk()
    root.title("Pomodoro Timer - Edited by 排隊Tim Wong")
    root.resizable(0,0)
    app = Application(root)
    app.configure(background="white")
    root.mainloop()