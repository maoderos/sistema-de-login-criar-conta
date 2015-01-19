from tkinter import *

def criar_conta():


root = Tk()
root.title('Crie sua conta')
Label(root, text="digite seu ID:").pack()

user_new = StringVar()
new_user= Entry(root, textvariable= user_new).pack()
Label(root, text="digite sua senha:").pack()

password_new = StringVar()
new_password = Entry(root, textvariable=password_new).pack()
Button(root, text='Criar conta', command= criar_conta).pack()
 
