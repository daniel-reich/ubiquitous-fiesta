
def even_or_odd(s):
  odd_sum = sum(int(x) for x in s if int(x) % 2 != 0)
  even_sum = sum(int(y) for y in s if int(y) % 2 == 0)
    
  d = {
  odd_sum > even_sum: 'Odd is greater than Even',
  even_sum > odd_sum: 'Even is greater than Odd',
  odd_sum == even_sum: 'Even and Odd are the same'}
  
  return d[True]

