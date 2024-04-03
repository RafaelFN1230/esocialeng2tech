#Heleno
from tkinter import *
from tkinter import filedialog
import pdfplumber

from funcoes import extrair_tabela
caminho_PDF = ""

def obter_dados():
    global caminho_PDF

    btnSelecionarPDF.config(state=DISABLED)

    status_label.config(text="Selecione o PDF ... Por favor!")

    try:
        # caminho_PDF = filedialog.askopenfilename(title="Selecione o arquivo PDF")

        # Abrir o arquivo PDF
        caminho_PDF = pdfplumber.open(filedialog.askopenfilename(title="Selecione o arquivo PDF"))

        vPagIni.set(1) #int(entPagIni.get())
        vPagFin.set(len(caminho_PDF.pages)) #int(entPagFin.get())

        # dados_por_pag = extrair_tabela(caminho_PDF, pagina_inicial, pagina_final)

        # nome_arquivo_excel = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Arquivos Excel", "*.xlsx")])
        # salvar_excel(dados_por_pag, nome_arquivo_excel)

        status_label.config(text="PDF selecionado com sucesso!")

    except Exception as e:
        status_label.config(text=f"Erro: {str(e)}")

    btnSelecionarPDF.config(state=NORMAL)

def extrair_xlsx():
    global caminho_PDF

    btnSelecionarPDF.config(state=DISABLED)
    btnGerarPDF.config(state=DISABLED)

    status_label.config(text="Extraindo dados... Por favor, aguarde.")

    try:
        extrair_tabela(caminho_PDF, vPagIni.get(), vPagFin.get())

        status_label.config(text="Extração concluída com sucesso!")

    except Exception as e:
        status_label.config(text=f"Erro: {str(e)}")

    btnSelecionarPDF.config(state=NORMAL)
    btnGerarPDF.config(state=NORMAL)

app = Tk()
app.geometry("300x200") 
app.minsize(300, 200) 
app.maxsize(300, 200)
app.resizable(width=0, height=0)
app.title("Extraindo xlsx de PDF")

vPagIni = StringVar()
vPagFin = StringVar()

frQuadro = Frame(app, borderwidth=1, relief="solid")
frQuadro.place(x=20, y=10, width=260, height=100)

# Dados Páginal Inicial - Label e Entry
lblPagIni = Label(frQuadro, text="Informe a página inicial:", font=("Arial", 10))
lblPagIni.place(x=20, y=20)#label_pagina_inicial.grid(row=1, column=0, padx = 10, pady = 20)
entPagIni = Entry(frQuadro, textvariable=vPagIni)
entPagIni.place(x=180, y=20, width=55)#entrada_pagina_inicial.grid(row=1, column=1)

# Dados Páginal Final - Label e Entry
lblPagFin = Label(frQuadro, text="Informe a página final:", font=("Arial", 10))
lblPagFin.place(x=20, y=60) # label_pagina_final.grid(row=5, column=0)

entPagFin = Entry(frQuadro, textvariable=vPagFin)
entPagFin.place(x=180, y=60, width=55) # entrada_pagina_final.grid(row=5, column=1)

# Dados Botão Selecionar - Label e Button foreground="#fff"
btnSelecionarPDF = Button(app, text="Selecionar PDF", background="#558", command=obter_dados)
btnSelecionarPDF.place(x=50, y=130)
#botao_selecionar_pdf.grid(row=9, column=0, columnspan=2)
#btnSelecionarPDF.pack(side=LEFT, fill=X, expand=TRUE)

# Dados Botão Selecionar - Label e Button foreground="#fff"
btnGerarPDF = Button(app, text="Gerar PDF", background="#fff", command=extrair_xlsx)
btnGerarPDF.place(x=170, y=130)

status_label = Label(app, text="Aguardando processamento ...")
status_label.place(x=20, y=180)
#status_label.grid(row=9, column=0, columnspan=2)

app.mainloop()