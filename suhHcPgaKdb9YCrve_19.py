
def even_or_odd(s):
  even, odd = 0, 0
  
  for i in s:
    i = int(i)
    if i % 2 == 0:
      even += i
    else:
      odd += i
      
  if even > odd: return 'Even is greater than Odd'
  elif odd > even: return 'Odd is greater than Even'
  else: return 'Even and Odd are the same'

