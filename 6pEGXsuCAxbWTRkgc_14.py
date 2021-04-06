
def loves_me(n):
  
  even = 'Loves me not'
  odd = 'Loves me'
  
  tr = []
  
  for num in range(1, n+1):
    if num == n:
      if num%2 == 0:
        tr.append(even.upper())
      else:
        tr.append(odd.upper())
    elif num%2 == 0:
      tr.append(even)
    else:
      tr.append(odd)
  
  return ', '.join(tr)

