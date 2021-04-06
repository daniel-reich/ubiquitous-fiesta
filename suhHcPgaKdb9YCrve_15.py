
def even_or_odd(s):
  o = sum(int(c) for c in s if c in '13579')
  e = sum(int(c) for c in s if c not in '13579')
​
  if o == e:
    return 'Even and Odd are the same'
​
  return ('Odd is greater than Even', 'Even is greater than Odd')[e > o]

