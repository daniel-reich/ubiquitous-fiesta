
def val(s):
  return int(s.replace('$','').replace(',',''))
​
def items_purchase(store, wallet):
  return sorted([item for item in store if val(store[item])<=val(wallet)]) or 'Nothing'

