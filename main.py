from tkinter import *
from tkinter.ttk import Entry,Button,OptionMenu
from tkinter import filedialog as tkFileDialog

class Main():
    def __init__(self, parent):
        self.parent=parent
        self.timeBetween=IntVar()
        self.error=0
        self.createWidgets()

    def createWidgets(self):
        #pads so that everything is spaced evenly
        padx=30
        pady=30

        self.mainFrame = Frame(self.parent)

        #title
        Label(self.mainFrame,text = 'Time to get focused!',font = ('',25)).pack(padx=padx,pady=pady)
        Button(self.mainFrame,text='Start',command=self.start).pack(padx=padx,pady=1)
        frame = Frame(self.mainFrame) #frame within main frame

        #time in between alerts
        Label(frame,text = 'Time in between alerts: ').grid(sticky=W)
        Entry(frame,textvariable = self.timeBetween,width=80).grid(row=0,column=1,padx=padx,pady=10)

        #finalizations
        frame.pack(padx=padx,pady=pady)
        self.mainFrame.pack()

    def start(self):
        timer=self.timeBetween.get()
        if timer<0: self.ShowError("You entered negative value for time interval :(")
        elif timer==0: self.ShowError("Please enter the length of the timer!")
        elif timer:
            print("exists")

    def ShowError(self, string):
        if self.error: self.error.pack_forget()
        self.error = Label(self.mainFrame,text = f'Error: {string}')
        self.error.pack(pady=10)


class Application(Frame):
    def __init__(self,parent,*args,**kwargs):
        Frame.__init__(self,parent,*args,**kwargs)


if __name__=="__main__":
    root=Tk()
    Main(root)
    root.mainloop()
