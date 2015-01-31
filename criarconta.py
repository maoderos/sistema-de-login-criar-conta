#cria conta e salva as mesmas no banco de dados
import tkinter 
import sqlite3


class Criar_conta(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.initialize()

    def initialize(self):
        self.user_new = tkinter.StringVar()
        self.password_new = tkinter.StringVar()
        self.email_new = tkinter.StringVar()
        self.check_create = tkinter.StringVar()
        self.labl1 = tkinter.Label(self, text='Digite seu ID').pack()
        self.entry = tkinter.Entry(self, textvariable=self.user_new).pack()
        self.labl2 = tkinter.Label(self, text='Digite sua senha').pack()
        self.entry2 = tkinter.Entry(self, textvariable=self.password_new).pack()
        self.labl3 = tkinter.Label(self, text='Digite seu email').pack()
        self.entry3 = tkinter.Entry(self, textvariable=self.email_new).pack()
        self.labl4 = tkinter.Label(self, textvariable=self.check_create).pack()
        self.button = tkinter.Button(self, text='criar conta', command=self.create_account).pack(side=tkinter.RIGHT)
        self.button2 = tkinter.Button(self, text="sair", command=self.sair).pack(side = tkinter.LEFT)
        
    def create_account(self):
        try:
            self.con = sqlite3.connect('login.sqlite')
            self.cursor = self.con.cursor()
            self.cursor.execute("""
                       INSERT INTO ids(id, senha, email)
                       VALUES (?,?,?)""",
                       (self.user_new.get(),
                        self.password_new.get(),
                        self.email_new.get()))
            self.con.commit()
            self.check_create.set('sua conta foi criada com sucesso')
            self.con.close()

        except Exception as err:
            self.check_create.set(str(err))
            self.con.commit()
            self.con.close()

    def sair(self):
        self.root = root
        self.root.destroy()
    
root = Criar_conta()
root.title('criar conta')
root.geometry("220x200")
root.mainloop()
            
