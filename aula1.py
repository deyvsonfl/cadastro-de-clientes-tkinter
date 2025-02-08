from tkinter import *

window = Tk()

class Application():

  def __init__(self):
    self.window = window
    self.display()
    self.display_frames()
    self.widgets_frame1()
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

  def widgets_frame1(self):
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

    # Criação da label do código
    self.lb_code = Label(self.frame_1, text = 'Código', bg='#dfe3ee')
    self.lb_code.place(relx=0.05, rely=0.06)
    # Criação da entrada do código
    self.entry_code = Entry(self.frame_1)
    self.entry_code.place(relx=0.05, rely=0.16, relwidth=0.09, relheight=0.09)

    # Criação da label do nome do cliente
    self.lb_client_name = Label(self.frame_1, text = 'Nome do cliente', bg='#dfe3ee')
    self.lb_client_name.place(relx=0.05, rely=0.36)
    # Criação da entrada do nome do cliente
    self.entry_client_name = Entry(self.frame_1)
    self.entry_client_name.place(relx=0.05, rely=0.46, relwidth=0.80, relheight=0.09)

    # Criação da label do telefone
    self.lb_phone = Label(self.frame_1, text = 'Telefone', bg='#dfe3ee')
    self.lb_phone.place(relx=0.05, rely=0.60)
    # Criação da entrada do telefone
    self.entry_phone = Entry(self.frame_1)
    self.entry_phone.place(relx=0.05, rely=0.70, relwidth=0.35, relheight=0.09)

     # Criação da label doa cidade
    self.lb_city = Label(self.frame_1, text = 'Cidade', bg='#dfe3ee')
    self.lb_city.place(relx=0.5, rely=0.60)
    # Criação da entrada do telefone
    self.entry_city = Entry(self.frame_1)
    self.entry_city.place(relx=0.5, rely=0.70, relwidth=0.35, relheight=0.09)

Application()