#pip install pdfplumber
#python.exe -m pip install --upgrade pip

import pdfplumber
import pandas as pd

# Abrir o arquivo PDF
pdf_path = "listaexcel.pdf"
pdf = pdfplumber.open(pdf_path)

# Salvar DataFrame em um arquivo Excel
#caminho_excel = "output.xlsx"

#pdf.pages
#pdf.metadata
totpag = len(pdf.pages)

for pag in range(1):
    pagina = pdf.pages[pag]

    tabela = pagina.extract_tables()

    # Salvar a primeira tabela como um arquivo XLS - len(tabela)
    df1 = pd.DataFrame()
    for qtd in range(len(tabela)):
        df1 = pd.DataFrame(data=tabela[qtd], dtype=object)
        #df1 = df1.dropna(how="all", axis=0) data=tabela[qtd], , columns=tabela[qtd] 
        #df1 = df1.dropna()
        #df1 = df1.ffill(); merge concat; merge_cells=True, float_format=None, encoding=_NoDefault.no_default, columns=None,sheet_name='Sheet1',

        df1Populado = df1.values

        if (df1Populado[0][1] != ""):
          df1.to_excel("planilha-pag_"+str(pag)+"_tab_"+str(qtd)+".xlsx", header=False, index=False)

# Converter tabela para DataFrame do pandas
#df = pd.concat(tabelas)