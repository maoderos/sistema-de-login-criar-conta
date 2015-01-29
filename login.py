''' interface do submit - usuario/senha'''
import tkinter
import sqlite3

class Login(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.initialize()

    def initialize(self):
        self.usuario = tkinter.StringVar()
        self.senha = tkinter.StringVar()
        self.labl1 = tkinter.Label(self, text="Por favor digite seu login e senha").pack()
        self.labl2 = tkinter.Label(self, text="Login:")
        self.entry1 = tkinter.Entry(self, textvariable=self.usuario).pack()
        self.labl3 = tkinter.Label(self, text='senha:').pack()
        self.entry2 = tkinter.Entry(self, textvariable=self.senha).pack()
        self.check = tkinter.StringVar()
        self.labl4 = tkinter.Label(self, textvariable=self.check).pack()
        self.button = tkinter.Button(self, text='entrar', command=self.fazer_login).pack(side=tkinter.LEFT)
        #self.button2 = tkinter.Button(self, text='Criar conta', command=self.criar_conta).pack(side = tkinter.RIGHT)

    def criar_conta(self):
         pass

    def fazer_login(self):
        try:
            self.con = sqlite3.connect('login.sqlite')
            self.cursor = self.con.cursor()
            self.cursor.execute('SELECT senha FROM ids WHERE id = "%s"' % self.usuario.get())
            self.dados = self.cursor.fetchall()
            self.dados_str = str(self.dados)
            
            (self.nda, self.senhas, self.nad) = self.dados_str.strip().split("'")
            
            if self.senha.get() == self.senhas:
                self.check.set('login concluido!')
                self.con.close()
            else:
                self.check("seu ID ou senha estao incorretos")
                self.con.close()
                
        except Exception as err:
            self.check.set('seu ID ou senha estao incorretos')
            self.con.close()
     
        
            
app = Login()
app.title('login')
app.mainloop()






