
def even_or_odd(s):
    odd = []
    even = []
    for i in s:
      if int(i)%2==0: even.append(int(i))
      else: odd.append(int(i))
    if sum(even) < sum(odd): return 'Odd is greater than Even'
    if sum(even) == sum(odd): return 'Even and Odd are the same'
    return 'Even is greater than Odd'

