''' interface do submit - usuario/senha'''
from tkinter import *
import sqlite3

def conta_criar():
    import criarconta

def login():
    try:
     con = sqlite3.connect('login.sqlite')
     cursor = con.cursor()
     cursor.execute('SELECT senha FROM ids WHERE id = "%s"' % usuario.get())
     dados = cursor.fetchall()
     dados_str = str(dados)
    
     (nada, senhas, nad) = dados_str.strip().split("'")
     if senha.get() == senhas:
         incorrect.set('login concluido!')
     else:
         incorrect.set('seu ID ou senha estao incorretos')
     con.close()
    except:
         incorrect.set("seu ID ou senha estao incorretos")
         con.close()
       


 
appli = Tk()
appli.title("i dont know yet")
Label(appli, text = "Por favor digite seu login e senha").pack()
Label(appli, text = "Login:").pack()

usuario = StringVar()
usuario_entry = Entry(appli, textvariable = usuario)
usuario_entry.pack()


Label(appli, text = "senha:").pack()
senha = StringVar()
senha_entry = Entry(appli, textvariable = senha)
senha_entry.pack()

incorrect = StringVar()
Label(appli, textvariable = incorrect).pack()
Button(appli, text='entrar', command=login ).pack(side=LEFT)
#Button(appli, text='crie uma conta', command=conta_criar).pack(side=RIGHT)


appli.mainloop()
