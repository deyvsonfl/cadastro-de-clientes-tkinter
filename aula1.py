from tkinter import *

window = Tk()

class Application():

  def __init__(self):
    self.window = window
    self.display()
    self.display_frames()
    self.create_buttons()
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

  def create_buttons(self):
    # Criação do botão limpar
    self.bt_clear = Button(self.frame_1, text="Limpar")
    self.bt_clear.place(relx=0.2, rely=0.1, relwidth=0.09, relheight=0.13)
    # Criação do botão buscar
    self.bt_search = Button(self.frame_1, text="Buscar")
    self.bt_search.place(relx=0.3, rely=0.1, relwidth=0.09, relheight=0.13)
     # Criação do botão novo
    self.bt_new = Button(self.frame_1, text="Novo")
    self.bt_new.place(relx=0.5, rely=0.1, relwidth=0.09, relheight=0.13)
     # Criação do botão alterar
    self.bt_change = Button(self.frame_1, text="Alterar")
    self.bt_change.place(relx=0.6, rely=0.1, relwidth=0.09, relheight=0.13)
     # Criação do botão apagar
    self.bt_erase = Button(self.frame_1, text="Apagar")
    self.bt_erase.place(relx=0.7, rely=0.1, relwidth=0.09, relheight=0.13)

Application()