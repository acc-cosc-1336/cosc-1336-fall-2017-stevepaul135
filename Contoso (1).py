from tkinter import Tk, Frame
from gui.frames.AboutFrames import AboutFrame
from gui.frames.StudentFrame import StudentFrame
from gui.frames.CourseFrame import CourseFrame
from Enrollment_Frame import EnrollmentFrame
from gui.main_menu import MainMenu
from navigation_bar import NavigationBar
from search_dialog import SearchDialog


from data.school_db import SchoolDB
from data.school_initializer import SchoolInitializer

class ContosoApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        Tk.wm_title(self, 'Contoso University')

        self.school_db = SchoolDB(SchoolInitializer())
        

        self.menubar = MainMenu(self)
        self.config(menu = self.menubar)

        self.frames = {}
        self.__init_frames()

    def __init_frames(self):

        container = Frame(self)
        container.pack(side ='top', fill ='both', expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight =1)

        for frame in (AboutFrame, CourseFrame, EnrollmentFrame, StudentFrame):
            if frame.__name__ == "About Frame":
                current_frame = frame(container)
            else:
                current_frame =frame(container, self.school_db)
                
           
            self.frames[frame.__name__] = current_frame
            current_frame.grid(row=0, column =0, sticky = 'nsew')

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        Tk.wm_title(self, 'Contoso University -' + frame_name.replace('Frame', '')) 
        frame.tkraise()

    def savedata(self):
        self.school_db.save_data()

    def on_search(self):

        search_string = SearchDialog(self, "Enter enroll id:").show()

        enrollment_list = self.data_source.data[int(search_string)]
        self.data_source.set_current_record(enrollment_list[0])
        self.data_grid.on_set_record(enrollment_list[0])


        

        
        

app = ContosoApp()
app.geometry('640x400')
app.mainloop()
