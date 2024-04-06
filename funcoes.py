#pip install pdfplumber
#python.exe -m pip install --upgrade pip

import pandas as pd

def extrair_tabela(filePDF, pagIni, pagFin):  
    pdf = filePDF
    years = [] 
    excel_path = "planilha-ficha_financeira ("+pagIni+"-"+pagFin+").xlsx"
    current_year = None

    dataset = {
        'periodo':{
            'elementos': {}
            }, 
        'proventos':{
            'elementos': {}
            }, 
        'descontos':{
            'elementos': {}
            }, 
        'totais':{
            'elementos': {}
            }
        }


    for pag in range(int(pagIni)-1, int(pagFin)):
        pagina = pdf.pages[pag]
        tabelas = pagina.extract_tables()
        tabela = tabelas[0]
        unwanted_columns = []
        dataset['descontos']['status'] = False
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
            if dado[0] == 'DESCONTOS':
                dataset['descontos']['status'] = True
            _add_element(dataset, dado[0], dado, years[0], current_year)

    final_dataset = _create_list(dataset)
    _generate_excel(final_dataset['chaves'], final_dataset['elementos'], excel_path)

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


def _add_element(dataset, chave, elementos:list, first_year, current_year):
    if chave in ['TOTAL DE PROVENTOS', 'TOTAL DE DESCONTOS', 'TOTAL LÍQUIDO A RECEBER']:
        _separa_elementos(dataset, chave, elementos,first_year, current_year, destino = 'totais')
    elif dataset['descontos']['status']:
        _separa_elementos(dataset, chave, elementos,first_year, current_year, destino = 'descontos')
    elif chave == 'PERÍODO':
        _separa_elementos(dataset, chave, elementos,first_year, current_year, destino = 'periodo')
    else:
        _separa_elementos(dataset, chave, elementos, first_year, current_year, destino = 'proventos')


def _create_list(dictionary:dict):
    lista = {'chaves': [], 'elementos': []}
    _junta_elementos(dictionary['periodo']['elementos'], lista)
    _junta_elementos(dictionary['proventos']['elementos'], lista)
    _junta_elementos(dictionary['descontos']['elementos'], lista)
    _junta_elementos(dictionary['totais']['elementos'], lista)
    return lista

def _fix_timeline(elementos:list, first_year:int, current_year:int):
    difference_in_years = current_year - first_year
    n_linhas = (difference_in_years*len(elementos))-difference_in_years
    if difference_in_years>0:
        for _ in range(n_linhas):
            elementos.insert(1, '')
    return elementos

def _separa_elementos (dataset, chave, elementos, first_year, current_year, destino):
    if chave in dataset[destino]['elementos']:
            for elemento in elementos:
                if elemento != chave:
                    dataset[destino]['elementos'][chave].append(elemento)
    else:
        elementos = _fix_timeline(elementos, first_year, current_year)
        dataset[destino]['elementos'][chave] = elementos

def _junta_elementos(dictionary:dict, lista:dict):
    for chave, valores in dictionary.items():
        lista['chaves'].append(chave)
        lista['elementos'].append(valores)        
    return lista