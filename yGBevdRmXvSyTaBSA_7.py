
from operator import itemgetter
def sort_drinks_by_price(drinks):
  return sorted(drinks, key=itemgetter('price'))

