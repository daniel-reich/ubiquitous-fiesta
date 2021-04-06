
from operator import itemgetter
def sort_drinks_by_price(d):
    return sorted(d, key=itemgetter('price'))

