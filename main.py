from tkinter import *
from tkinter.ttk import Entry,Button,OptionMenu
import time

class Main():
    def __init__(self, parent):
        self.parent=parent
        self.timeBetween=IntVar()
        self.alert=BooleanVar()
        self.error=0
        self.choices=['Hours','Seconds','Minutes','Hours']
        self.choice=StringVar(parent)
        self.createWidgets()

    def createWidgets(self):
        #pads so that everything is spaced evenly
        padx=30
        pady=30
        textframe=0

        self.mainFrame = Frame(self.parent)

        #title box
        Label(self.mainFrame,text = 'Time to get focused!',font = ('',25)).pack(padx=padx,pady=pady)
        Button(self.mainFrame,text='Start',command=self.start).pack(padx=padx,pady=1)
        frame = Frame(self.mainFrame) #frame within main frame


        #time-in-between-alerts text input box
        textframe = Frame(frame, width=100, height=50)
        textframe.columnconfigure(0, weight=10)
        textframe.grid_propagate(False)

        Entry(textframe,textvariable = self.timeBetween,width=80).grid(sticky="we",pady=15)
        self.timeBetween.set(61)

        #time-in-between-alerts label
        Checkbutton(frame, text='Time in between alerts: ',variable=self.alert, onvalue=1, offvalue=0, command = lambda : self.toggle(textframe)).grid(sticky='W')
        Label(frame,text = '').grid(sticky='W')

        #time-in-between-alerts text options
        OptionMenu(frame, self.choice, *self.choices).grid(row=0,column=2,padx=15,pady=10)
        self.choice.set('Seconds')

        #finalizations
        textframe.grid(row=0,column=1,padx=padx,pady=10)
        frame.pack(padx=padx,pady=pady)
        self.mainFrame.pack()
        self.toggle(textframe)

    def toggle(self,frame):
        if self.alert.get()==1:
            for child in frame.winfo_children(): child.configure(state='enable')
        if self.alert.get()==0:
            for child in frame.winfo_children(): child.configure(state='disable')

    def start(self):
        timer=self.timeBetween.get()
        if timer<0: self.ShowError("You entered negative value for time interval :(")
        elif timer==0: self.ShowError("Please enter the length of the timer!")
        elif timer<60 and self.choice.get()=='Seconds': self.ShowError("Please a higher interval (a minute or more)")
        elif timer:
            app = Application(self.parent)
            self.mainFrame.pack_forget()
            app.pack()

    def ShowError(self, string):
        if self.error: self.error.pack_forget()
        self.error = Label(self.mainFrame,text = f'Error: {string}')
        self.error.pack(pady=5)


class Application(Frame):
    def __init__(self,parent,*args,**kwargs):
        Frame.__init__(self,parent,*args,**kwargs)
        Button(self,text='End',command=self.end).pack(padx=100,pady=100)

    def end(self):
        print("hello")


if __name__=="__main__":
    root=Tk()
    Main(root)
    root.mainloop()
