#pip install pdfplumber
#python.exe -m pip install --upgrade pip

import pdfplumber
import pandas as pd

def extrair_tabela(filePDF, pagIni, pagFin):  
    # Abrir o arquivo PDF
    pdf = filePDF
    date = [] 
    dataset = []
    for pag in range(int(pagIni)-1, int(pagFin)): # paginaInicial, paginaFinal
        pagina = pdf.pages[pag]
        tabelas = pagina.extract_tables()
        tabela = tabelas[0]
        unwanted_columns = []
        # Salvar a primeira tabela como um arquivo XLS - len(tabela)
        df1 = pd.DataFrame()
        for index, coluna in enumerate(tabela):
            if coluna[0].lower() in ['dados bancários', 'banco', 'agência', 'conta']:
                unwanted_columns.append(index)
            elif coluna.count('') == len(coluna):
                unwanted_columns.append(index)
            elif coluna.count(None) == len(coluna)-1:
                pass
            elif 'JAN/' in coluna[1]:
                for value in coluna:
                    date.append(value)
                unwanted_columns.append(index)
            #print('coluna: ',coluna)
        tabela = _dataset_cleaner(tabela, unwanted_columns)
        for clean_colunm in tabela:
            dataset.append(clean_colunm)

        print('dataset: ', dataset)
            
        for qtd in range(len(tabela)):
            df1 = pd.DataFrame(data=tabela[qtd], dtype=object)

            df1Populado = df1.values

            if (df1Populado[0][1] != ""):
                df1.to_excel("planilha-pag_"+str(pag+1)+"_tab_"+str(qtd)+".xlsx", sheet_name="eSocial", header=False, index=False)

def _dataset_cleaner(dataset, unwanted_columns):
    unwanted_columns.reverse()
    for index in unwanted_columns:
      dataset.pop(index)
    return dataset

