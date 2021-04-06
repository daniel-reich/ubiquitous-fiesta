
from operator import mul
​
def order_people(lst, people):
  if mul(*lst) < people:
    return 'overcrowded'
  
  itr = iter(range(1, people + 1))
  func = lambda: [next(itr, 0) for _ in range(lst[1])]
  return [func() if i%2 == 0 else func()[::-1]
                for i in range(lst[0])]

