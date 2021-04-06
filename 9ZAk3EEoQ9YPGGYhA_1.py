
import re
​
def price(string):
  return int(re.sub('[^\d]', '', string))
​
def items_purchase(store, wallet):
  return sorted(
    key for key, value in store.items() 
    if price(value) <= price(wallet)
  ) or 'Nothing'

