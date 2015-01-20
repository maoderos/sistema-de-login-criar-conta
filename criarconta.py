from tkinter import *
import sqlite3

def criar_conta():
    con = sqlite3.connect('logindata.sqlite')
    cursor = con.cursor()
    cursor.execute("""
                   INSERT INTO ids(id, senha, email)
                   VALUES (?,?,?)""",
                   (user_new.get(), password_new.get(), email_new.get()))
    con.commit()

     


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
Button(root, text='Criar conta', command= criar_conta).pack()
 
