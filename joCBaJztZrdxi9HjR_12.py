
def tp_checker(h):
  
  days = int( (h['tp'] * 500) / (h['people'] * 57 ) )
  msg = 'Your TP will '
​
  if days < 14: 
    msg += 'only last {} days, buy more!'.format(days)
  else:
    msg += 'last {} days, no need to panic!'.format(days)
​
  return msg

