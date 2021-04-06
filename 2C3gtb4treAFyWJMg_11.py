
def polybius(text):
    import string
    num=[str(a)+str(b) for a in range(1,6) for b in range(1,6)]
    num.append('24')
    alpha=list(string.ascii_lowercase)
    alpha.append(alpha.pop(9))
    res=[]
    list1=[]
    if text[0].lower() in alpha:
        for i in range(len(text)):
            if text[i].lower() in alpha:
                res.append(num[alpha.index(text[i].lower())])
            elif text[i]==" ":
                res.append(" ")
        return "".join(res)
    text=text.split(" ")
    for i in text:
        for x in range(0,len(i)-1,2):
            list1.append(i[x]+i[x+1])
        list1.append(" ")
    for i in range(len(list1)):
            if list1[i] in num:
                res.append(alpha[num.index(list1[i])])
            else:
                res.append(" ")
    return "".join(res)[0:-1]

