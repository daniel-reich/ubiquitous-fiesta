
def can_enter_cave(listString):
    listA = listString
    A = listA[0]
    B = listA[1]
    C = listA[2]  
    D = listA[3]
    if len(listA) == 5:
        E = listA[4]     
    a = False
    b = 1
    for i in range(len(A) - 1):
        if len(listA) == 5:
            if A[i] + A[b] == 0 or B[i] + B[b] == 0 or C[i] + C[b] == 0 or D[i] + D[b] == 0 or E[i] + E[b] == 0:
                a = True
            else:
                a = False
                break
            b += 1
        else:
            if A[i] + A[b] == 0 or B[i] + B[b] == 0 or C[i] + C[b] == 0 or D[i] + D[b] == 0:
                a = True
            else:
                a = False
                break
            b += 1    
    return a

