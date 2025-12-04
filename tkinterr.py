from tkinter import *


root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        root.mainloop()
    def tela(self):
        self.root.title("Minha janela")
        self.root.configure(background="Gray")
        self.root.geometry("700x500")
        self.root.resizable(True,True)
        self.root.maxsize(width=900,height=700)
        self.root.minsize(width=400,height=300)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.02 ,rely=0.02,relwidth=0.96,relheight=0.5)

Application()