from tkinter import *
from tkinter.ttk import Entry,Button,OptionMenu
from tkinter import filedialog as tkFileDialog

class Main():
    def __init__(self, parent):
        self.parent=parent
        self.timeBetween=IntVar()
        self.createWidgets()

    def createWidgets(self):
        #pads so that everything is spaced evenly
        padx=30
        pady=30

        self.mainFrame = Frame(self.parent)
        Label(self.mainFrame,text = 'Time to get focused!',font = ('',25)).pack(padx=padx,pady=pady)

        frame = Frame(self.mainFrame) #frame within main frame
        Label(frame,text = 'Time to get focused!').grid(sticky=W)
        Entry(frame,textvariable = self.timeBetween,width=80).grid(row=0,column=1,padx=padx,pady=pady)
        #Label(frame,text = 'Image').grid(sticky=W)
        frame.pack(padx=padx,pady=pady)

        self.mainFrame.pack()


if __name__=="__main__":
    root=Tk()
    Main(root)
    root.mainloop()
