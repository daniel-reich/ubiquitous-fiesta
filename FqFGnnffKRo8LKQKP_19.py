
def simple_numbers(a, b):
    # 135 = 1^1 + 3^2 + 5^3
    L = [];
    for i in range(a,b+1):
        if isSimpleNumber(i):
            L.append(i);
    return L;
    
def isSimpleNumber(n):
    C = 0;
    for i in range(1,len(str(n))+1):
        #print(i,C,str(n)[i-1])
        C+= int(str(n)[i-1])** i;
    return C == n

