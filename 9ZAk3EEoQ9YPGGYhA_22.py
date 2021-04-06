
def items_purchase(store, wallet):
  arr = []
  for x in store:
    if int(store[x].replace("$","").replace(",","")) <= int(wallet.replace("$","").replace(",","")):
      arr.append(x)
  if len(arr) > 0:
    return sorted(arr)
  else : return "Nothing"

