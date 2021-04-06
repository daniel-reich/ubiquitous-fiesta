
def even_or_odd(s):
  even=sum(int(x) for x in s if int(x)%2==0)
  odd=sum(int(x) for x in s if int(x)%2)
  return 'Even is greater than Odd' if even>odd else \
  'Odd is greater than Even' if odd>even else 'Even and Odd are the same'

