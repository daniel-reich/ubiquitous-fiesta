
def unstretch(word):
    lis = list(word)
    i=0
    j=1
    while j <len(lis):
        if lis[i]==lis[j]:
            lis.pop(j)
            j=i+1
        else:
            i +=1
            j +=1
    result=''
    for char in lis:
        result +=char
    return result

