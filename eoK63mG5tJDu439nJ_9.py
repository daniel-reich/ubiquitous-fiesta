
import numpy as np
def levenshtein(seq1, seq2):
    a=[]
    x = len(seq1) + 1
    y = len(seq2) + 1
    m= np.zeros ((x,y))
    for x in range(x):
        m[x, 0] = x
    for y in range(y):
        m[0, y] = y
    z=[]    
    for x in range(0,x):
        for y in range(0,y):
            if seq1[x-1] == seq2[y-1]:
                m[x,y] = min(m[x-1, y] + 1, m[x-1, y-1],m[x, y-1] + 1)                
            else:
                m[x,y] = min(m[x-1,y] + 1,m[x-1,y-1] + 1,m[x,y-1] + 1) 
        a.append(int(m[x - 1,y - 1]))
    return a
def isWordChain(words):
    for word in range(len(words)-1):
        x=[]
        seq1=words[word]
        seq2=words[word+1]
        x.append((levenshtein(seq1,seq2))) 
    print(x) 
    if x[0][2]!=1or x[0][-1]==1:
        return True
    else:
        return False

