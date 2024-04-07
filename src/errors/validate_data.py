import pdfplumber
from src.errors.errors import *
import os

def validate_user_input_file(caminho_PDF:str):
    if type(caminho_PDF) != pdfplumber.pdf.PDF:
        if caminho_PDF == '':
            raise MissingUserInputFile
        
        elif not caminho_PDF.lower().endswith('.pdf'):
            print(caminho_PDF.lower().endswith('.pdf'))
            print(os.path.basename(caminho_PDF))
            raise WrongUsersInputFileType
    
def validate_user_input_data(vPagIni:str, vPagFin:str, vPagTotal:int):    
    if vPagIni == '' or vPagIni == None:
        raise MissingUserInput
    
    elif vPagFin == '' or vPagFin == None:
        raise MissingUserInput
    
    elif not vPagIni.isnumeric() or not vPagFin.isnumeric():
        raise WrongUsersInputDataType

    elif int(vPagIni) < 1:
        raise OutOfBoundsInicial
    
    elif int(vPagFin) > vPagTotal:
        raise OutOfBoundsFinal
    
    elif int(vPagIni) > int(vPagFin):
        raise InicialPageBiggerThanFinalPage