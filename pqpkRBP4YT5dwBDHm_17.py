
def lowestnum(x=list):
    lowest=x[0]
    for y in x:
        if y<lowest:
            lowest=y
    return lowest
# now we assign the lowest number in the list in the function
def show_the_love(lst=list):
    a=lowestnum(lst)
    f=0
    for number in lst:
        if number!=a:
            b=number*(3/4)
            c=lst.index(number)
            lst.remove(number)
            lst.insert(c,b)
            f+=number*(1/4)
    d=lst.index(a)
    lst.remove(a)
    lst.insert(d,f+a)
    return lst

