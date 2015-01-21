#cria conta e salva as mesmas no banco de dados
from tkinter import *
import sqlite3


def conta_criar():
    try:
        con = sqlite3.connect('login.sqlite')
        cursor = con.cursor()
        cursor.execute("""
                       INSERT INTO ids(id, senha, email)
                       VALUES (?,?,?)""",
                       (user_new.get(),
                        password_new.get(),
                        email_new.get()))
        con.commit()
        stats.set('sua conta foi criada com sucesso')
        con.close()
    except Exception as err:
        stats.set(str(err))
        con.close()
      


root = Tk()
root.title('Crie sua conta')
Label(root, text="digite seu ID:").pack()

user_new = StringVar()
new_user= Entry(root, textvariable= user_new).pack()
Label(root, text="digite sua senha:").pack()

password_new = StringVar()
new_password = Entry(root, textvariable=password_new).pack()

Label(root, text="digite seu endereço de email:").pack()
email_new = StringVar()

new_email = Entry(root, textvariable=email_new).pack()

stats = StringVar()
Label(root, textvariable=stats).pack()
Button(root, text='Criar conta', command= conta_criar).pack()
Button(root, text="sair", command=root.destroy).pack()

root.mainloop() 

 
