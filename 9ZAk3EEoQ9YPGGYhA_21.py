
def items_purchase(store, wallet):
    l = list(store.items())
    lprice = list(map(lambda x:int(x[1].replace(',','')[1:]),l))
    ans = []
    for i in range(len(lprice)):
        if int(wallet[1:])>=lprice[i]:ans.append(l[i][0])
    return  sorted(ans) if len(ans)!=0 else 'Nothing'

