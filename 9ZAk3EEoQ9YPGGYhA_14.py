
import re
def items_purchase(store, wallet):
  USD = lambda n: int(''.join(re.findall(r'\d+', n)))
  return sorted(k for k, v in store.items() if USD(v) <= USD(wallet)) or 'Nothing'

