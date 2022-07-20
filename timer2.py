import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import queue
import time
#from playsound import playsound
import winsound
import platform


class StopWatch(threading.Thread):

    def __init__(self, queue,h, m, s, stopwatch):
        threading.Thread.__init__(self)


        self.queue = queue
        self.check = True
        self.h = h.get()
        self.m = m.get()
        self.s = s.get()
        self.t = (h.get() * 3600 + m.get() * 60 + s.get())
        self.stopwatch = stopwatch
        self.is_play = None

    def stop(self):
        flags = winsound.SND_FILENAME
        winsound.PlaySound(None, flags)
        self.check = False


    def play_sound(self, sound_file,):

        try:
            # Windows
            if platform.system() == 'Windows':
                flags = winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP
                winsound.PlaySound(sound_file, flags)
            # Linux
            elif platform.system() == "Linux":
                os.system("aplay -q {}&".format(sound_file))
        except:
            messagebox.showwarning(self.parent.title(), "Time over.", parent=self)


    def run(self):

        for i in range(0,self.t):

            if i == (self.t-1):
                file=os.path.join('sounds', "alarm.wav")
                self.play_sound(file)


            if not self.check:
                self.is_play=None

                break

            if self.s !=0:
                self.s -= 1
            else:
                self.s = 59
                if self.m !=0:
                    self.m -=1
                else:
                    if self.h !=0:
                        self.h -=1
                        self.m = 59

            clock = (self.h, self.m, self.s)
            self.queue.put(clock)
            time.sleep(1)

        self.check = False


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.queue = queue.Queue()
        self.clock = None

        self.h =  tk.IntVar()
        self.m =  tk.IntVar()
        self.s =  tk.IntVar()

        self.vcmd = (self.register(self.validate), '%d', '%P', '%S')

        self.init_ui()

    def init_ui(self):

        self.pack(fill=tk.BOTH, expand=1)

        f = ttk.Frame()

        ttk.Label(f, text = "Stopwach").pack()

        w = tk.LabelFrame(f, borderwidth=1)

        d = tk.Spinbox(w, bg='white', fg='blue',width=2, from_=0, to=24,
                       validate = 'key',
                       validatecommand = self.vcmd,
                       textvariable=self.h,relief=tk.GROOVE,)

        m = tk.Spinbox(w, bg='white',fg='blue', width=2, from_=0, to=60,
                       validate = 'key',
                       validatecommand = self.vcmd,
                       textvariable=self.m,relief=tk.GROOVE,)

        y = tk.Spinbox(w, bg='white', fg='blue',width=4, from_=0, to=60,
                       validate = 'key',
                       validatecommand = self.vcmd,
                       textvariable=self.s,relief=tk.GROOVE,)

        for p,i in enumerate((d,m,y)):
            i.pack(side=tk.LEFT, fill=tk.X, padx=2)

        w.pack()

        f.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5, expand=1)

        w = ttk.Frame()

        ttk.Button(w, text="Start", command=self.on_start).pack()
        ttk.Button(w, text="Stop", command=self.on_stop).pack()
        ttk.Button(w, text="Close", command=self.on_close).pack()

        f.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        w.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

    def on_start(self, evt=None):

        try:
            self.clock = StopWatch(self.queue,self.h,self.m,self.s,self)
            self.clock.start()
            self.periodic_call()

        except :
            msg = "Format error:\n%s"%str(sys.exc_info()[1])
            messagebox.showerror(self.parent.title(), msg, parent=self)



    def on_stop(self,evt=None):
        self.clock.stop()

    def on_close(self, evt=None):
        self.clock.stop()
        self.parent.on_exit()

    def periodic_call(self):

        self.check_queue()
        if self.clock.is_alive():
            self.after(1, self.periodic_call)
        else:
            pass

    def check_queue(self):
        while self.queue.qsize():
            try:
                x = self.queue.get(0)
                self.h.set(x[0])
                self.m.set(x[1])
                self.s.set(x[2])

            except queue.Empty:
                pass

    def validate(self, action, value, text,):
        # action=1 -> insert
        if(action=='1'):
            if text in '0123456789':
                try:
                    int(value)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True              

class App(tk.Tk):
    """Start here"""

    def __init__(self):
        super().__init__()

        self.protocol("WM_DELETE_WINDOW", self.on_exit)

        self.set_title()
        self.set_style()

        frame = Main(self,)
        frame.pack(fill=tk.BOTH, expand=1)

    def set_style(self):
        self.style = ttk.Style()
        #('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        self.style.theme_use("clam")


    def set_title(self):
        s = "{0}".format('Simple App')
        self.title(s)

    def on_exit(self):
        """Close all"""
        if messagebox.askokcancel("Simple App", "Do you want to quit?", parent=self):
            self.destroy()               

if __name__ == '__main__':
    app = App()
    app.mainloop()