
def id_mtrx (n) :
    if isinstance (n, int) == False :
        return 'Error'
    elif n >= 0 :
        return  ([[1 if i == j else 0 for i in range (n)] for j in range (n)])
    else :
        return  ([[1 if i == -n-j-1 else 0 for i in range (-n)] for j in range (-n)])

