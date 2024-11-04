import tkinter as tk
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
from pandastable import Table


janela = Tk()
janela.title("Gerenciador de Planilhas")
janela.attributes("-fullscreen", False)


class ExcelEditor:
    def __init__(self, janela_principal):

        self.janela_principal = janela_principal  

        self.resultado_label = Label(self.janela_principal, text="Total: ", font="Arial 16", bg="#F5F5F5")
        self.resultado_label.pack(side=TOP, padx=10, pady=10)

        #Cria um dataframe vazio, uma tabela no excel
        self.df = pd.DataFrame()


        #Inicializar as variaveis
        self.tree = None
        self.table = None 
        self.filename = ""

        self.cria_widgets()

    def cria_widgets(self):
        menu_bar = tk.Menu(self.janela_principal)


        menu_arquivos = tk.Menu(menu_bar, tearoff=0)

        menu_arquivos.add_command(label="Abrir", command=janela.destroy)
        menu_arquivos.add_separator()

        menu_arquivos.add_command(label="Salvar como", command=janela.destroy)
        menu_arquivos.add_separator()


        menu_arquivos.add_command(label="Sair", command=janela.destroy)
        

        menu_bar.add_cascade(label="Arquivo", menu=menu_arquivos)
        
        #Define a barra de menu como a barra de menu da janela principal
        self.janela_principal.config(menu=menu_bar)


    
editor = ExcelEditor(janela)


janela.mainloop()





