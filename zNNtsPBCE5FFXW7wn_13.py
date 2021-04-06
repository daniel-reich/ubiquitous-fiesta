
def empty_values(lst):
    a = []
    for i in lst:
        if type(i)==int:
            a.append(0)
        elif type(i)==float:
            a.append(0.0)
        elif type(i)==str:
            a.append('')
        elif type(i)==bool:
            a.append(False)
        elif type(i)==list:
            a.append([])
        elif type(i)==tuple:
            a.append(())
        elif type(i)==set:
            a.append(set())
        elif i==None:
            a.append(None)
​
    return a

