
def items_purchase(store, wallet):
  return (sorted(a for (a,b) in store.items() 
    if int(b[1:].replace(',','')) <= int(wallet[1:].replace(',','')))
    or 'Nothing')

