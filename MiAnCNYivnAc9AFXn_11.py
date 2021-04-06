
def change_types(lst):
    k=[]
    for i in lst:
        if type(i)==int :
            if i%2==0:
                i=i+1
                k.append(i)
            else:
                k.append(i)
        elif type(i)==bool:
            i=not i
            k.append(i)
        else:
            i=i.title()
            i=i+'!'
            k.append(i)
    return k

