
from string import ascii_uppercase
​
def playfair(txt, keyword):
    ## Format strings
    
    decipher = False
    if txt.isalpha() and txt.isupper():
        decipher = True
    else:
        txt = txt.upper()
        aux = []
        for a in txt:
            if a.isalpha():
                aux.append(a)
        txt = "".join(aux)
    
    keyword = keyword.upper()
    keyword = "".join([j for i, j in enumerate(keyword) if j not in keyword[:i]])
    
    ## Create polybius square
    
    n = 5
    char_list = list(keyword) + [c for c in ascii_uppercase if c not in keyword]
    char_list.remove('J')
    
    square = [[""]*n for i in range(n)]
    for i in range(n):
        row = []
        for j in range(n):
            c = char_list[j + n*(i)]
            if c != 'J':
                square[i][j] = c
    
    ## Prepare digraphs
    
    digraphs = []
    i = 0
    while i < len(txt):
        if i == len(txt)-1 or txt[i] == txt[i+1]:
            digraphs.append((txt[i] if txt[i] != "J" else "I", "X"))
            i += 1
        else:
            digraphs.append((txt[i] if txt[i] != "J" else "I", txt[i+1] if txt[i] != "J" else "I"))
            i += 2
    print(digraphs)
    
    ## Cipher
    
    c_digraphs = []
    for d in digraphs:
        first = None
        second = None
        for i, row in enumerate(square):
            if first is None:
                first = (i, row.index(d[0])) if d[0] in row else None
            if second is None:
                second = (i, row.index(d[1])) if d[1] in row else None
            if first and second:
                break
            
        if first[0] == second[0]:
            if decipher:
                c_digraphs.append(((square[first[0]][first[1]-1] if first[1]-1 >= 0 else square[first[0]][-1]),
                    (square[second[0]][second[1]-1] if second[1]-1 >= 0 else square[second[0]][-1])))
            else:
                c_digraphs.append(((square[first[0]][first[1]+1] if first[1]+1 < len(square[0]) else square[first[0]][0]),
                    (square[second[0]][second[1]+1] if second[1]+1 < len(square[0]) else square[second[0]][0])))
        elif first[1] == second[1]:
            if decipher:
                c_digraphs.append(((square[first[0]-1][first[1]] if first[0]-1 >= 0 else square[-1][first[1]]),
                    (square[second[0]-1][second[1]] if second[0]-1 >= 0 else square[-1][second[1]])))
            else:
                c_digraphs.append(((square[first[0]+1][first[1]] if first[0]+1 < len(square) else square[0][first[1]]),
                    (square[second[0]+1][second[1]] if second[0]+1 < len(square) else square[0][second[1]])))
        else:
            c_digraphs.append((square[first[0]][second[1]], square[second[0]][first[1]]))
    return "".join(list(map(lambda x: x[0]+x[1], c_digraphs)))

