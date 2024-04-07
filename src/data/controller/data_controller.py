from src.data.utils.util import fix_timeline

def dataset_cleaner(dataset:list, unwanted_columns:list):
    unwanted_columns.reverse()
    for index in unwanted_columns:
        dataset.pop(index)
    return dataset

def add_element(dataset, chave, elementos:list, first_year, current_year):
    if chave in ['TOTAL DE PROVENTOS', 'TOTAL DE DESCONTOS', 'TOTAL LÍQUIDO A RECEBER']:
        separa_elementos(dataset, chave, elementos,first_year, current_year, destino = 'totais')
    elif dataset['descontos']['status']:
        separa_elementos(dataset, chave, elementos,first_year, current_year, destino = 'descontos')
    elif chave == 'PERÍODO':
        separa_elementos(dataset, chave, elementos,first_year, current_year, destino = 'periodo')
    else:
        separa_elementos(dataset, chave, elementos, first_year, current_year, destino = 'proventos')

def separa_elementos (dataset, chave, elementos, first_year, current_year, destino):
    if chave in dataset[destino]['elementos']:
            for elemento in elementos:
                if elemento != chave:
                    dataset[destino]['elementos'][chave].append(elemento)
    else:
        elementos = fix_timeline(elementos, first_year, current_year)
        dataset[destino]['elementos'][chave] = elementos

