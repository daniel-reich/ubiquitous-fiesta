
def batting_avg(lst):
 totalx = 0
 totaly = 0
 for x,y in lst:
  totalx += x
  totaly += y
 if len(str(totalx/totaly)) == 4:
  return str(totalx/totaly)[1:] + '0'
 else:
  return str(round((totalx/totaly),3))[1:]

