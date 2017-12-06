from tkinter import Tk

from gui.main_menu import MainMenu

class ContosoApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        Tk.wm_title(self, 'Contoso University')

        self.menubar = MainMenu(self)
        self.config(menu = self.menubar)

app = ContosoApp()
app.geometry('640x400')
app.mainloop()

             
