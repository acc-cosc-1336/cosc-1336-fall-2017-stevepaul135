from tkinter import Frame, Label

class CourseFrame(Frame):
    """ Frame Container for the about screen"""

    def __init__(self, parent):
        Frame.__init__(self,parent)

        Label(self, text= "Course Frame").grid(row =0, column =0, sticky ='w')
