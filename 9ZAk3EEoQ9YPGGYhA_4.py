
import re
​
def items_purchase(store, wallet):
  wallet = int(re.sub('\$|\,', '', wallet))
  store = {k: int(re.sub('\$|\,', '', v)) for k, v in store.items()}
  
  lst = sorted(i for i, j in store.items() if j <= wallet)
  
  if not lst:
    return 'Nothing'
  return lst

