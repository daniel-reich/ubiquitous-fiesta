
def decode(txt):
    list=[]
    for i in txt:
        sum=0
        a=ord(i)
        for i in str(a):
            sum+=int(i)
        list.append(sum)
    return list

