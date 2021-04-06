
def items_purchase(store,wallet):
    newlst = []
    for x,y in store.items():
        y = y.replace(",","")
        if int(wallet[1:]) >= int(y[1:]):
            newlst.append(x)
    return sorted(newlst) if newlst else "Nothing"

