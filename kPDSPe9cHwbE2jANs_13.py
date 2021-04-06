
def cards_needed(n):
  if(n < 0):
    return "invalid"
  return 3*(n*(n+1)/2) - n

