
def even_or_odd(s):
  e = sum(int(i) for i in s if int(i)%2==0)
  o = sum(int(i) for i in s if int(i)%2)
  
  if e == o:
      return 'Even and Odd are the same'
  if e > o:
    return 'Even is greater than Odd'
  return 'Odd is greater than Even'

