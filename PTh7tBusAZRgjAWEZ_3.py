
def calc_diff(obj, limit):
  totalval = 0
  for x in obj:
    totalval += obj[x]
  return(totalval - limit)

