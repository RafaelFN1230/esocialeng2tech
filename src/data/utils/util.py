import os

import pdfplumber

def fix_timeline(elementos:list, first_year:int, current_year:int):
    difference_in_years = current_year - first_year
    n_linhas = (difference_in_years*len(elementos))-difference_in_years
    if difference_in_years>0:
        for _ in range(n_linhas):
            elementos.insert(1, '')
    return elementos

def get_filename(filePDF:pdfplumber.pdf.PDF, pagIni, pagFin):  
    pdf = filePDF
    file = os.path.basename(pdf.stream.name)
    file_name = os.path.splitext(file)[0] 
    excel_path = f"{file_name} Ficha Financeira pg({pagIni} - {pagFin}).xlsx"
    return excel_path