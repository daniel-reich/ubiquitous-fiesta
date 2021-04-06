
def lucky_seven(lst):
  if not lst and len(lst)<3 and sum(lst)<7: return False
  from itertools import combinations as comb
  for c in comb(lst, 3):
    if sum(c)==7:
      return True
  return False

