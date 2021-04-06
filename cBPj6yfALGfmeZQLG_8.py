
def vertical_txt(txt):
    result = []
    txt = txt.split()
    longest = len(sorted(txt, reverse=True, key=len)[0])
    
    for i in range(len(txt)):
        if len(txt[i]) < longest:
            txt[i] = txt[i] + " " * (longest - len(txt[i]))
    
    for j in range(longest): 
        add = []
        for i in range(len(txt)):
            add += txt[i][j]
        result.append(add)
        
    return result

