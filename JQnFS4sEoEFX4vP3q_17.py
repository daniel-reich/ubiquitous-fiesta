
from itertools import combinations as comb
from functools import reduce
def product_pair(lst, k):
  if k > len(lst):
    return
  prod_lst = [reduce(lambda x,y:x*y,each) for each in comb(lst,k)]
  return (min(prod_lst),max(prod_lst))

