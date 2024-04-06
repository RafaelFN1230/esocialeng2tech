#pip install pdfplumber
#python.exe -m pip install --upgrade pip

import pandas as pd

def extrair_tabela(filePDF, pagIni, pagFin):  
    pdf = filePDF
    years = [] 
    dataset = {}
    excel_path = "planilha-ficha_financeira ("+pagIni+"-"+pagFin+").xlsx"
    current_year = None

    for pag in range(int(pagIni)-1, int(pagFin)):
        pagina = pdf.pages[pag]
        tabelas = pagina.extract_tables()
        tabela = tabelas[0]
        unwanted_columns = []
        for index, coluna in enumerate(tabela):
            if coluna[0].lower() in ['dados bancários', 'banco', 'agência', 'conta']:
                unwanted_columns.append(index)
            elif coluna.count('') == len(coluna):
                unwanted_columns.append(index)
            elif coluna.count(None) == len(coluna)-1:
                pass
            elif 'JAN/' in coluna[1]:
                periodo = coluna[1].split('/')
                if int(periodo[1]) not in years:
                    coluna[0] = 'PERÍODO'
                    _add_element(dataset, coluna[0], coluna, 0, 0)
                    current_year = int(periodo[1])
                    years.append(current_year)
                unwanted_columns.append(index)
        dados = _dataset_cleaner(tabela, unwanted_columns)
        for dado in dados:
            _add_element(dataset, dado[0], dado, years[0], current_year)

    final_daset = _create_list(dataset)
    _generate_excel(final_daset['chaves'], final_daset['elementos'], excel_path)

def _dataset_cleaner(dataset:list, unwanted_columns:list):
    unwanted_columns.reverse()
    for index in unwanted_columns:
        dataset.pop(index)
    return dataset

def _generate_excel(chaves, elementos, excel_path):
    df = pd.DataFrame(elementos, index=chaves).T

    for indice_linha, linha in df.iterrows():
        for coluna, valor_celula in linha.items():
            if coluna != 'PERÍODO':
                if valor_celula != None and valor_celula != '':
                    if valor_celula not in chaves:
                        valor_celula = float(valor_celula.replace('.', '').replace(',', '.'))
                        df.at[indice_linha, coluna] = valor_celula
    df.to_excel(excel_path, sheet_name="eSocial", index=False, header=False)


def _add_element(dicionario, chave, elementos:list, first_year, current_year):
    if chave in dicionario:
        for elemento in elementos:
            if elemento != chave:
                dicionario[chave].append(elemento)
    else:
        elementos = _fix_timeline(elementos, first_year, current_year)
        dicionario[chave] = elementos


def _create_list(dictionary:dict):
    chaves = []
    elementos = []

    for chave, valores in dictionary.items():
        chaves.append(chave)
        elementos.append(valores)
    list = {'chaves':chaves, 'elementos':elementos}
    return list

def _fix_timeline(elementos:list, first_year:int, current_year:int):
    difference_in_years = current_year - first_year
    n_linhas = (difference_in_years*len(elementos))-difference_in_years
    if difference_in_years>0:
        for _ in range(n_linhas):
            elementos.insert(1, '')
    return elementos
