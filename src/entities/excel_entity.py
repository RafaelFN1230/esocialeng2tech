import pandas as pd

def generate_excel(chaves, elementos, excel_path):
    df = pd.DataFrame(elementos, index=chaves).T

    for indice_linha, linha in df.iterrows():
        for coluna, valor_celula in linha.items():
            if coluna != 'PERÍODO':
                if valor_celula != None and valor_celula != '':
                    if valor_celula not in chaves:
                        valor_celula = float(valor_celula.replace('.', '').replace(',', '.'))
                        df.at[indice_linha, coluna] = valor_celula
    df.to_excel(excel_path, sheet_name="eSocial", index=False, header=False)