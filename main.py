#Heleno
from tkinter import *
from tkinter import filedialog
import pdfplumber

from src.use_cases.extract_table import extrair_tabela
caminho_PDF = ""

def obter_dados():
    global caminho_PDF

    btnSelecionarPDF.config(state=DISABLED)

    status_label.config(text="Selecione o PDF ... Por favor!")

    try:
        # Abrir o arquivo PDF
        caminho_PDF = pdfplumber.open(filedialog.askopenfilename(title="Selecione o arquivo PDF"))

        vPagIni.set(1)
        vPagFin.set(len(caminho_PDF.pages))

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
lblPagIni.place(x=20, y=20)
entPagIni = Entry(frQuadro, textvariable=vPagIni)
entPagIni.place(x=180, y=20, width=55)

# Dados Páginal Final - Label e Entry
lblPagFin = Label(frQuadro, text="Informe a página final:", font=("Arial", 10))
lblPagFin.place(x=20, y=60)

entPagFin = Entry(frQuadro, textvariable=vPagFin)
entPagFin.place(x=180, y=60, width=55)

# Dados Botão Selecionar - Label e Button
btnSelecionarPDF = Button(app, text="Selecionar PDF", background="#558", command=obter_dados)
btnSelecionarPDF.place(x=50, y=130)

# Dados Botão Selecionar - Label e Button
btnGerarPDF = Button(app, text="Gerar PDF", background="#fff", command=extrair_xlsx)
btnGerarPDF.place(x=170, y=130)

status_label = Label(app, text="Aguardando processamento ...")
status_label.place(x=20, y=180)

app.mainloop()