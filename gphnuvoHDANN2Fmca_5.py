
def odd_sort(lst):
  odds = sorted([elt for elt in lst if elt%2==1],reverse=True)
  return [odds.pop() if elt%2==1 else elt for elt in lst]

