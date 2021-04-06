
def sum_neg(lst):
  if lst:
    return [len([nmbr for nmbr in lst if nmbr > 0]), sum([nmbr for nmbr in lst if nmbr < 0])] 
  else:
    return []

