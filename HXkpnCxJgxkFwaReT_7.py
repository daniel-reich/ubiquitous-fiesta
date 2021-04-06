
def count_datatypes(*args):
    inteiros, string, booleano, lista, tupla, dicionario = 0, 0, 0, 0, 0, 0
    for n in args:
        if type(n) == int:
            inteiros = inteiros+1
        elif type(n) == str:
            string = string+1
        elif type(n) == bool:
            booleano = booleano+1
        elif type(n) == tuple:
            tupla = tupla+1
        elif type(n) == dict:
            dicionario = dicionario+1
        elif type(n) == list:
            lista=lista+1
    vetor = [inteiros, string, booleano, lista, tupla, dicionario]
    return vetor

