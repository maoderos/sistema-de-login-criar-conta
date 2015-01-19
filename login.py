''' interface do submit - usuario/senha'''
from tkinter import *


def conta_criar():
    import criarconta

 


def login():
 


 
app = Tk()
app.title("i dont know yet")
Label(app, text = "Por favor digite seu login e senha").pack()
Label(app, text = "Login:").pack()

usuario = StringVar()
usuario_entry = Entry(app, textvariable = usuario)
usuario_entry.pack()


Label(app, text = "senha:").pack()
senha = StringVar()
senha_entry = Entry(app, textvariable = senha)
senha_entry.pack()

incorrect = StringVar()
Label(app, textvariable = incorrect).pack()
Button(app, text='entrar', command=login).pack(side=LEFT)
Button(app, text='crie uma conta', command=conta_criar).pack(side=RIGHT)

app.mainloop()

