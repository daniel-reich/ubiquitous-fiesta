
def count_digits(lst,t):
    b=[]
    lst1=[str(i) for i in lst]
    if t=='even':
        for i in lst1:
            k=0
            for j in range(len(i)):
                if int(i[j])%2==0:
                    k+=1
            b.append(k)
    else:
        for i in lst1:
            k=0
            for j in range(len(i)):
                if int(i[j])%2 != 0:
                    k+=1
            b.append(k)
        
    return b

