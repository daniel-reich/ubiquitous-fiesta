
def esPrimo(numero):
    for i in range(2,numero-1):
        if (numero%i)==0:
            return(False)
    return(True)
    
def goldbach_conjecture(numero):
    salida=[]
    auxiliar=[]
    if (numero%2)==1:
        return(salida)
    else:
        for i in range(2, numero):
            if(esPrimo(i)):
                auxiliar.append(i)
        print(auxiliar)
        q = len(auxiliar)
        print(q)
        for x in range (q):
            print(q-x)
            bigger=auxiliar[q-x-1]
            print(bigger)
            for aux in auxiliar:
                if aux + bigger == numero:
                    salida.append(aux)
                    salida.append(bigger)
                    return (salida)

