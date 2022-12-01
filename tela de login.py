import tkinter
from t

root = Tk()

class App():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.txt()
        self.bt()
        self.grid()
        root.mainloop()

    def tela(self):
        self.root.title("Tela de login")
        self.root.geometry("350x300+610+153")
        self.root.configure(background="#DCDCDC")
        self.root.resizable(False,False)

    def txt(self):
        self.tex1 = tkinter.Label(self.root,text="Login",font=('Gotham',26 ), bg="#DCDCDC",fg='black')
        self.tex1.place(relx=0.02, rely=0.04)

        self.tex2 = tkinter.Label(self.root, text="Nome *", font=('Gotham', 14), bg="#DCDCDC", fg='black')
        self.tex2.place(relx=0.04, rely=0.25)

        self.tex3 = tkinter.Label(self.root, text="Senha *", font=('Gotham', 14), bg="#DCDCDC", fg='black')
        self.tex3.place(relx=0.04, rely=0.5)
    def grid(self):
        self.gd = tkinter.Entry(self.root, font=('Gotham', 14))
        self.gd.place(relx=0.04, rely=0.38, relheight=0.08, relwidth=0.90)

        self.gd2 = tkinter.Entry(self.root, font=('Gotham', 14))
        self.gd2.place(relx=0.04, rely=0.63, relheight=0.08, relwidth=0.90)

    def frames(self):
        self.frame1 = Frame(self.root, bd=4, bg="#008080")
        self.frame1.place(relx=0.02,rely=0.20,relheight=0.02,relwidth=0.96)

    def bt(self):
        self.bt1 = Button(self.root,bd=3,bg="#008080",command="exit",text="Entrar",fg="#DCDCDC")
        self.bt1.place(relx=0.20,rely=0.80,relheight=0.10,relwidth=0.60)

App()