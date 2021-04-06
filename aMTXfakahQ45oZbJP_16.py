
def complete_bracelet(lst):
    
    step = 2
    
    while step < len(lst):
        valido = True
        lista = []
        if len(lst)%step == 0:
            for idx in range(0, len(lst), step):
                lista.append(lst[idx:idx+step])
            for idx in range(len(lista)):
                if lista[0] != lista[idx]:
                    valido = False
            if valido == True:
                return True
        step += 1       
    
    return False

