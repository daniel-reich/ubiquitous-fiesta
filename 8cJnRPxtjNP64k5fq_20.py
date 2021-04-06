
from operator import itemgetter
def dance(lst, p):
  women = list(map(itemgetter(0),lst))
  men = list(map(itemgetter(1),lst))
  if p == 'men':
    return [[x,y] for x,y in zip(women,men[::-1])]
  else:
    return [[x,y] for x,y in zip(women[::-1],men)]

