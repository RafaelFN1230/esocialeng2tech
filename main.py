#Heleno
from tkinter import *
from tkinter import filedialog
import pdfplumber

from src.use_cases.extract_table import extrair_tabela
from src.errors.errors import *
from src.errors.validate_data import validate_user_input_data, validate_user_input_file

class use_case_input:
    def __init__(self) -> None:
        self.caminho_PDF = ""
        self.excecoes_personalizadas = (
            MissingUserInputFile,
            MissingUserInput,
            OutOfBoundsFinal,
            OutOfBoundsInicial,
            InicialPageBiggerThanFinalPage,
            WrongUsersInputDataType,
            WrongUsersInputFileType,
            )

    def obter_dados(self):
        btnSelecionarPDF.config(state=DISABLED)

        status_label.config(text="Por favor, selecione um PDF")

        try:
            # Abrir o arquivo PDF
            selected_file = filedialog.askopenfilename(title="Selecione o arquivo PDF")
            validate_user_input_file(selected_file)
            self.caminho_PDF = pdfplumber.open(selected_file)

            vPagIni.set(1)
            vPagFin.set(len(self.caminho_PDF.pages))

            status_label.config(text="PDF selecionado com sucesso!")

        except self.excecoes_personalizadas as e:
            status_label.config(text=e.message)
            
        except Exception as e:
            status_label.config(text=f"Erro: {str(e)}")

        btnSelecionarPDF.config(state=NORMAL)

    def extrair_xlsx(self):
        btnSelecionarPDF.config(state=DISABLED)
        btnGerarPDF.config(state=DISABLED)

        status_label.config(text="Extraindo dados... Por favor, aguarde.")

        try:
            validate_user_input_file(self.caminho_PDF)
            validate_user_input_data(vPagIni.get(), vPagFin.get(), vPagTotal=len(self.caminho_PDF.pages))

            extrair_tabela(self.caminho_PDF, vPagIni.get(), vPagFin.get())

            status_label.config(text="Extração concluída com sucesso!")

        except self.excecoes_personalizadas as e:
            status_label.config(text=e.message)

        except Exception as e:
            status_label.config(text=f"Erro: {str(e)}")

        btnSelecionarPDF.config(state=NORMAL)
        btnGerarPDF.config(state=NORMAL)

UseCaseInput= use_case_input()

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
btnSelecionarPDF = Button(app, text="Selecionar PDF", background="#558", command=UseCaseInput.obter_dados)
btnSelecionarPDF.place(x=50, y=130)

# Dados Botão Selecionar - Label e Button
btnGerarPDF = Button(app, text="Gerar PDF", background="#fff", command=UseCaseInput.extrair_xlsx)
btnGerarPDF.place(x=170, y=130)

status_label = Label(app, text="Aguardando processamento ...")
status_label.place(x=20, y=180)

app.mainloop()