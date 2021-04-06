
def champions(ts):
  return max(ts, 
           key = lambda t: (3*t['wins']+t['draws'], t['scored']-t['conceded'])
         )['name']

