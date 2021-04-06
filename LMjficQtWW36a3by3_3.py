
def probability(lst, n):
  outcomes = 0
  for number in lst:
    if number >= n:
      outcomes += 1
  return round((outcomes/len(lst))*100,1)

