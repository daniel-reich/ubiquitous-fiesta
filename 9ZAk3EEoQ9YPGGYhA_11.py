
def items_purchase(store, wallet):
    m = int(wallet[1:]);
    l = [k for k,v in store.items() if int(v[1:].replace(",",""))<=m];
    if l:
        return sorted(l);
    return "Nothing"

