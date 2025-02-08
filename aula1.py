from tkinter import *

window = Tk()

class Application():
  def __init__(self):
    self.window = window
    self.tela()
    window.mainloop()
  def tela(self):
    self.window.title("Cadastro de Clientes")
    self.window.configure(background= '#fdfdfd')
    self.window.wm_maxsize(1280, 1080)
    self.window.wm_minsize(788, 588)
    self.window.resizable(True, True)

Application()