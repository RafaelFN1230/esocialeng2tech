#pip install pdfplumber
#python.exe -m pip install --upgrade pip
from src.entities.excel_entity import generate_excel
from src.data.builder.data_builder import create_list
from src.data.controller.data_controller import add_element, dataset_cleaner
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
                    add_element(dataset, coluna[0], coluna, 0, 0)
                    current_year = int(periodo[1])
                    years.append(current_year)
                unwanted_columns.append(index)
        
        dados = dataset_cleaner(tabela, unwanted_columns)
        for dado in dados:
            if dado[0] == 'DESCONTOS':
                dataset['descontos']['status'] = True
            add_element(dataset, dado[0], dado, years[0], current_year)

    final_dataset = create_list(dataset)
    generate_excel(final_dataset['chaves'], final_dataset['elementos'], excel_path)
