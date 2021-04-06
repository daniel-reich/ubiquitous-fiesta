
import re
​
def bird_code(lst):
    lista = []
    counter = 0
    for i in lst:
        i = re.split('[\s\-]', i)
        for j in i:
            if len(i) == 4:
                lista.append(j[0:1].upper())
            elif len(i) == 3:
                lista.append(j[0:1].upper())
                counter += 1
                if counter == 3:
                    lista.append(j[1:2].upper())
                    counter = 0
            elif len(i) == 2:
                lista.append(j[0:2].upper())
            elif len(i) == 1:
                lista.append(j[0:4].upper())
    lista = ''.join(lista)
    return re.findall('....', lista)

