
def comments_correct(txt):
    lst=[txt[i:i+2] for i in range(0, len(txt),2)]
    print(lst)
    dlst1=[]
    dlst2=[]
    for i in lst:
        if len(i) < 2:
            return False
        if i == "/*":
            dlst1.append(i)
        if i == "*/":
            dlst2.append(i)
    return len(dlst1) == len(dlst2)

