
def count_sub(L, s, H,A):
    if 1 in L:
        G = []
        x = L.index(1)
        G.append(1)
        for i in range(1, x + 1, 1):
            if L[x - i] == L[x] + i:
                G.append(L[x - i])
            else:
                break
        s += 1
​
        G.reverse()
        H.append(G)
        count_sub(L[x + 1:],s,H,A)
    else:
        if A==[]:
            A.append(s)
            A.append(H)
​
def final_countdown(L):
    A=[]
    H=[]
    s=0
    count_sub(L,s,H,A)
    return(A)

