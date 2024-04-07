def create_list(dictionary:dict):
    lista = {'chaves': [], 'elementos': []}
    junta_elementos(dictionary['periodo']['elementos'], lista)
    junta_elementos(dictionary['proventos']['elementos'], lista)
    junta_elementos(dictionary['descontos']['elementos'], lista)
    junta_elementos(dictionary['totais']['elementos'], lista)
    return lista

def junta_elementos(dictionary:dict, lista:dict):
    for chave, valores in dictionary.items():
        lista['chaves'].append(chave)
        lista['elementos'].append(valores)        
    return lista