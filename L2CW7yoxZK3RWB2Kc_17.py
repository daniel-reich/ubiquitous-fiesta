
def nico_cipher(message, key):
    
    sk=sorted(key)
    nl, temp, result =[], [], []    #nl:num list
    for i in key:
        if not sk.index(i) in nl: nl.append(sk.index(i))
        else: nl.append(sk.index(i)+1)
    
    
    ln = len(message)//len(key)+1 #line number
    sn = len(key) - (len(message) - (ln-1)*len(key)) #space number
    for i in range(ln): temp.append(list(message[len(key)*i:len(key)*(i+1)]))
    for i in range(sn): temp[-1].append(" ") 
    for i in temp:
        for j in range(len(key)): result. append(i[nl.index(j)])
    return "".join(result)

