
def sort_drinks_by_price(drinks):
  from operator import itemgetter
  return sorted(drinks,key=itemgetter("price"))

