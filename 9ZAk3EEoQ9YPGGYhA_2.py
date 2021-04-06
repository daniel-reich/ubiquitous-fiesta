
def items_purchase(store, wallet):
    res = sorted(k for k, val in store.items()
                 if int(val[1:].replace(',', '')) <= int(wallet[1:]))
    return res if res else "Nothing"

