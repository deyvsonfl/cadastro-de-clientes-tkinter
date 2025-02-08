from tkinter import *
from tkinter import ttk
import sqlite3

window = Tk()

class Functions():
  def clear_entry(self):
    self.entry_code.delete(0, END)
    self.entry_client_name.delete(0, END)
    self.entry_phone.delete(0, END)
    self.entry_city.delete(0, END)
  def db_connect(self):
    self.con = sqlite3.connect("clientes.db")
    self.cursor = self.con.cursor(); print("Conectando ao banco de dados...")
  def db_disconnect(self):
    self.con.close(); print("Desconectando ao banco de dados...")
  def create_tables(self):
    self.db_connect();
    ### Criar tabela
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS clientes(
        cod INTEGER PRIMARY KEY,
        client_name CHAR(40) NOT NULL,
        phone INTEGER(20),
        city CHAR(40)
      );
    """)
    self.con.commit(); print("Banco de dados criado")
    self.db_disconnect()
  def variables(self):
    self.code = self.entry_code.get()
    self.name = self.entry_client_name.get()
    self.phone = self.entry_phone.get()
    self.city = self.entry_city.get()
  def add_client(self):
    self.db_connect()
    self.variables()
    self.cursor.execute(""" INSERT INTO clientes (client_name, phone, city)
                        VALUES (?, ?, ?)""", (self.name, self.phone, self.city))
    self.con.commit()
    self.db_disconnect()
    self.select_list()
    self.clear_entry()
  def select_list(self):
    self.client_list.delete(*self.client_list.get_children())
    self.db_connect()
    list = self.cursor.execute(""" SELECT cod, client_name, phone, city FROM clientes ORDER BY client_name ASC; """)
    for i in list:
      self.client_list.insert("", END, values=i)
    self.db_disconnect()
  def OnDoubleClick(self, event):
    self.clear_entry()
    self.client_list.selection()

    for n in self.client_list.selection():
      col1, col2, col3, col4 = self.client_list.item(n, 'values')
      self.entry_code.insert(END, col1)
      self.entry_client_name.insert(END, col2)
      self.entry_phone.insert(END, col3)
      self.entry_city.insert(END, col4)
  def client_delete(self):
    self.variables()
    self.db_connect()
    self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.code))
    self.con.commit()
    self.db_disconnect()
    self.clear_entry()
    self.select_list()

class Application(Functions):
  def __init__(self):
    self.window = window
    self.display()
    self.display_frames()
    self.widgets_frame1()
    self.frame2_list()
    self.create_tables()
    self.select_list()
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
    self.bt_clear = Button(self.frame_1, text="Limpar", command= self.clear_entry)
    self.bt_clear.place(relx=0.2, rely=0.1, relwidth=0.09, relheight=0.13)
    # Criação do botão buscar
    self.bt_search = Button(self.frame_1, text="Buscar")
    self.bt_search.place(relx=0.3, rely=0.1, relwidth=0.09, relheight=0.13)
     # Criação do botão novo
    self.bt_new = Button(self.frame_1, text="Novo", command=self.add_client)
    self.bt_new.place(relx=0.5, rely=0.1, relwidth=0.09, relheight=0.13)
     # Criação do botão alterar
    self.bt_change = Button(self.frame_1, text="Alterar")
    self.bt_change.place(relx=0.6, rely=0.1, relwidth=0.09, relheight=0.13)
     # Criação do botão apagar
    self.bt_erase = Button(self.frame_1, text="Apagar", command=self.client_delete)
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
  def frame2_list(self):
    self.client_list = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", 'col3', 'col4'))
    self.client_list.heading("#0", text="")
    self.client_list.heading("#1", text="Código")
    self.client_list.heading("#2", text="Nome")
    self.client_list.heading("#3", text="Telefone")
    self.client_list.heading("#4", text="Cidade")

    self.client_list.column("#0", width=1, stretch=NO)
    self.client_list.column("#1", width=50)
    self.client_list.column("#2", width=200)
    self.client_list.column("#3", width=125)
    self.client_list.column("#4", width=125)

    self.client_list.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

    self.scrollList = Scrollbar(self.frame_2, orient='vertical')
    self.client_list.configure(yscrollcommand=self.scrollList.set)
    self.scrollList.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
    self.client_list.bind("<Double-1>", self.OnDoubleClick)

Application()