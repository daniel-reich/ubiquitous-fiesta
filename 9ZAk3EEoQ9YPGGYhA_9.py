
def items_purchase(store, wallet):
    L = [k for k in list(store.keys()) if int(store[k][1:].strip(',').replace(',', '')) <= int(wallet.strip('$'))]
    if len(L)==0:
        return "Nothing"
    L.sort()
    return L

