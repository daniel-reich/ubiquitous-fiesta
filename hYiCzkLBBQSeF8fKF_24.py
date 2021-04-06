
def count(deck):
  sum = 0
  for element in deck:
    try:
      if element < 7:
        sum = sum + 1
      elif element == 10:
        sum = sum - 1
    except TypeError:
      sum = sum - 1
  return(sum)

