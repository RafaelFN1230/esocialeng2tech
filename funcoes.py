#pip install pdfplumber
#python.exe -m pip install --upgrade pip

import pdfplumber
import pandas as pd

def extrair_tabela(filePDF, pagIni, pagFin):  
  # Abrir o arquivo PDF
  pdf = filePDF
 
  for pag in range(int(pagIni)-1, int(pagFin)): # paginaInicial, paginaFinal
      pagina = pdf.pages[pag]
      tabela = pagina.extract_tables()

      # Salvar a primeira tabela como um arquivo XLS - len(tabela)
      df1 = pd.DataFrame()
      for qtd in range(len(tabela)):
          df1 = pd.DataFrame(data=tabela[qtd], dtype=object)

          df1Populado = df1.values

          if (df1Populado[0][1] != ""):
            df1.to_excel("planilha-pag_"+str(pag+1)+"_tab_"+str(qtd)+".xlsx", sheet_name="eSocial", header=False, index=False)
