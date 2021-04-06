
def items_purchase(store, wallet):
  amount = int(wallet.replace("$",''))
  newlist = []
  for eachitem in store.keys():
    if int(store[eachitem].replace("$",'').replace(',','')) <= amount:
      newlist.append(eachitem)
  if newlist == []:
    return 'Nothing'
  else:
    return sorted(newlist)

