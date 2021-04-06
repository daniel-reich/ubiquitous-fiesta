
def find_the_falsehoods(lst):
    lst1 = []
    for elem in lst:
     
        x = bool(elem)
        if x == False:   
            lst1.append(elem)
    return lst1

