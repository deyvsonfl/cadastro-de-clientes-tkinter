from tkinter import *

window = Tk()

class Application():
  def __init__(self):
    self.window = window
    self.display()
    self.display_frames()
    window.mainloop()
  def display(self):
    self.window.title("Cadastro de Clientes")
    self.window.configure(background= '#fdfdfd')
    self.window.wm_maxsize(1280, 1080)
    self.window.wm_minsize(788, 588)
    self.window.resizable(True, True)
  def display_frames(self):
    self.frame_1 = Frame(self.window, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
    self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

    self.frame_2 = Frame(self.window, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
    self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

  

Application()