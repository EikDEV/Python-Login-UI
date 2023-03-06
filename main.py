from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
import mysql.connector
root = Tk()

class Funcs():
    def conecta_db(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='pythonlogin'
        )
        self.cursor = self.conn.cursor()
    def desconecta_db(self):
        self.conn.close()
    def login(self):
        self.conecta_db()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        command = f'select name, email, password from users where email = "{email}" and password = "{senha}";'
        self.cursor.execute(command)
        result = self.cursor.fetchone()
        if result:
            msg = messagebox.showinfo("Aviso", "Logando...")
            print(result)
            self.tela1()
            self.desconecta_db()
        else:
            msg = messagebox.showwarning("Aviso", "E-mail ou senha inválidos.")
            self.desconecta_db()

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.widgets_root()
        root.mainloop()
    def tela(self):
        self.root.title("Login")
        self.root.configure(background='#fff')
        self.root.geometry("250x300")
        self.root.resizable(False, False)
    def widgets_root(self):
        self.lb_login = Label(self.root, text='Login', font=('monospace', 28), bg="#fff")
        self.lb_login.place(x=10, y=0)

        self.l_linha = Label(root, text='', width=220, anchor=NW, font=('monospace', 1), bg='#2596be')
        self.l_linha.place(x=10, y=50)

        self.lb_email = Label(self.root, text='Email', font=('monospace', 14), bg="#fff")
        self.lb_email.place(x=10, y=70)

        self.email_entry = Entry(self.root, bd=2, font=(14), borderwidth=1, highlightthickness=1, relief='solid')
        self.email_entry.place(x=10, y=100, width=230, height=30)

        self.lb_senha = Label(self.root, text='Senha', font=('monospace', 14), bg="#fff")
        self.lb_senha.place(x=10, y=150)

        self.senha_entry = Entry(self.root, bd=2, font=(14), borderwidth=1, highlightthickness=1, relief='solid')
        self.senha_entry.place(x=10, y=180, width=230, height=30)

        self.btn_entrar = Button(self.root, text='Entrar', command=self.login, bg="#2596be", fg="#fff", font=('monospace', 15))
        self.btn_entrar.place(x=10, y=230, width=230, height=30)
    def tela1(self):
        self.root1 = Toplevel()
        self.root1.title("Bem-vindo!")
        self.root1.configure(background='#fff')
        self.root1.geometry("600x500")
        self.root1.resizable(True, True)
        self.root1.transient(self.root)
        self.root1.focus_force()
        self.root1.grab_set()

Application()
