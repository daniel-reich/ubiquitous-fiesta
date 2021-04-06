
from operator import itemgetter
​
def chosen_wine(wines):
  if not wines:
    return None
  name = itemgetter('name')
  if len(wines) == 1:
    return name(wines[0])
  return name(sorted(wines, key=itemgetter('price'), reverse=True)[-2])

