from tkinter import Frame, Label

class StudentFrame(Frame):
    """ Frame Container for the about screen"""

    def __init__(self, parent):
        Frame.__init__(self,parent)

        Label(self, text= "Student Frame").grid(row =0, column =0, sticky ='w')
