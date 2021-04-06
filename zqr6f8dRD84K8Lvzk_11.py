
from math import sqrt
def hex_lattice(n):
    puntos=(n-1)/6
    capas=int(sqrt(puntos*2))
​
    for i in range(int(capas+1)):
        puntos-=i
    if puntos:
        return("Invalid")
    else:
        cad=""
        for i in range(-capas,capas+1):
            cad+=" "*(abs(i))+" "+"o "*(2*capas-abs(i)+1)+ " "*(abs(i))
        
            if i!=capas:
                cad+="\n"
​
        return cad

