
def even_or_odd(s):
  a,b = sum(map(int,s)),sum(int(i) for i in s if not int(i)%2)
  a = a-b
  return 'Odd is greater than Even' if b-a<0 else 'Even is greater than Odd' if b-a>0 else 'Even and Odd are the same'

