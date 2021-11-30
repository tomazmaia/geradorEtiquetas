from tkinter import *
from tkinter import ttk
import subprocess
import csv

class Gerador:

    def __init__(self,quadro):

        #Janela
        quadro.title("GERADOR DE ETIQUETAS")
        quadro.geometry("500x220")
        quadro.configure(background="DARKGREEN")
        quadro.resizable(width=False, height=False)
        quadro.attributes("-alpha",0.9)

        #Backgrounds Frames
        self.leftFrame = Frame(quadro, width=155, height=217, bg="BLACK", relief="raise")
        self.leftFrame.pack(side=LEFT)

        self.rightFrame = Frame(quadro, width=340, height=217, bg="MIDNIGHTBLUE", relief="raise")
        self.rightFrame.pack(side=RIGHT)

        #BOTOES
        btnGerar = ttk.Button(self.leftFrame, width=14, text="GERAR", command=self.gerar)
        btnGerar.place(x=20,y=35)

        btnLimpar = ttk.Button(self.leftFrame, width=14, text="LIMPAR", command=self.limpar)
        btnLimpar.place(x=20,y=80)

        btnAbout = ttk.Button(self.leftFrame, width=10, text="SAIR", command=lambda: self.sair())
        btnAbout.place(x=35, y=175)

        #LABELS DOS CAMPOS
        self.labelNome = Label(self.rightFrame, text="Nome Lógico", font=('Verdana','9','bold'), bg="MIDNIGHTBLUE", fg="White")
        self.labelNome.place(x=30, y=10)

        self.labelSerie = Label(self.rightFrame, text="Numero de série", font=('Verdana','9','bold'), bg="MIDNIGHTBLUE", fg="White")
        self.labelSerie.place(x=30, y=70)

        self.labelPat = Label(self.rightFrame, text="Patrimonio", font=('Verdana','9','bold'), bg="MIDNIGHTBLUE", fg="White")
        self.labelPat.place(x=30, y=135)

        #CAMPOS
        self.campoNome = Entry(self.rightFrame, width=20, font=('Verdana','14'))
        self.campoNome.focus_force()
        self.campoNome.place(x=43, y=35, height=25)

        self.campoSerie = Entry(self.rightFrame, width=20, font=('Verdana', '14'))
        self.campoSerie.focus_force()
        self.campoSerie.place(x=43, y=100, height=25)

        self.campoPat = Entry(self.rightFrame, width=20, font=('Verdana','14'))
        self.campoPat.focus_force()
        self.campoPat.place(x=43, y=165, height=25)

    def limpar(self):
        self.campoNome.delete(0,'end')
        self.campoSerie.delete(0,'end')
        self.campoPat.delete(0,'end')

    def gerar(self):
        nome = self.campoNome.get()
        serie = self.campoSerie.get()
        pat = self.campoPat.get()

        #Ajustes de espaços
        valor_reference = 24
        base = valor_reference * '-'

        valorNome = (valor_reference - 7) - len(nome)
        valorSerie = (valor_reference - 8) - len(serie)
        valorPat = (valor_reference - 7) - len(pat)

        espacoNome = valorNome * " " + '|\n'
        espacoSerie = valorSerie * " " + '|\n'
        espacoPat = valorPat * " " + '|\n'

        if len(nome) > 11:
            acrescimo = len(nome) - 11
            base = (len(base) + acrescimo) * '-'
            espacoNome = (len(espacoNome) - acrescimo) * " " + '|\n'
            espacoSerie = (len(espacoSerie) - acrescimo) * " " + '|\n'
            espacoPat = (len(espacoPat) - acrescimo) * " " + '|\n'

        with open('etiqueta.txt','w',encoding='utf-8') as etiqueta:
            etiqueta.write('+'+base+'+\n')
            etiqueta.write('| Nome: ' + nome.upper() + espacoNome)
            etiqueta.write('| Serie: ' + serie.upper() + espacoSerie)
            etiqueta.write('| Pat.: '+ pat.upper() + espacoPat)
            etiqueta.write('+'+base+'+')


        subprocess.call('/home/tomaz/Documentos/WORKSPACE/proj_G_Etiqueta/etiqueta.txt')

        pass



    def sair(self):
        self.destroy()