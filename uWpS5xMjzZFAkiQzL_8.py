
def odds_vs_evens(num):
  even,odd=0,0
  for i in str(num):
    if int(i)%2==0:
      even+=int(i)
    else:
      odd+=int(i)
  if even>odd:
    return "even"
  elif odd>even:
    return "odd"
  else:
    return "equal"

