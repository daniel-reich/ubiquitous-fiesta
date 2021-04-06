
def swap_cards(n1, n2):
    [n1, n2] = [list(map(lambda x:int(x),list(str(n1)))), list(map(lambda x:int(x),list(str(n2))))]
    min1 = min(*n1)
    n1[n1.index(min1)]=n2[0]
    n2[0] = min1
    return  int(''.join(list(map(lambda x:str(x),n1))))>int(''.join(list(map(lambda x:str(x),n2))))

