class MissingUserInputFile(Exception):
    def __init__(self, *args):
        self.message = "Por favor, forneça o arquivo PDF."

class MissingUserInput(Exception):
    def __init__(self, *args):
        self.message = "Forneça a página inicial e final."

class OutOfBoundsFinal(Exception):
    def __init__(self, *args):
        self.message = "Página final superior ao total de páginas no arquivo."

class OutOfBoundsInicial(Exception):
    def __init__(self, *args):
        self.message = "A página inicial deve ser maior ou igual a 1."

class InicialPageBiggerThanFinalPage(Exception):
    def __init__(self, *args):
        self.message = "A página inicial deve ser menor ou igual a final."

class WrongUsersInputDataType(Exception):
    def __init__(self, *args):
        self.message = "A página deve ser um número inteiro e positivo."

class WrongUsersInputFileType(Exception):
    def __init__(self, *args):
        self.message = "O arquivo deve ser do tipo PDF."