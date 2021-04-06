
def isbn10(m):
  sum10 = sum([int(m[i])*(10-i) for i in range(9)])
  if m[-1] == 'X':
    sum10 += 10
    m = m[:9] + '0'
  else:
    sum10 += int(m[-1])
  if sum10 % 11 != 0:
    return 'Invalid'
  else:
    newm = '978' + m
    r = 0
    while isbn13(newm) == 'Invalid':
      newm = newm[:12] + str(r)
      r += 1
    return newm
  
​
def isbn13(n):
  if len(n) == 10:
    return isbn10(n)
  sum13a = sum([3*int(n[i]) for i in range(1, 13, 2)])
  sum13b = sum([int(n[j]) for j in range(0, 13, 2)])
  sum13 = sum13a + sum13b
  if sum13 % 10 == 0:
    return 'Valid'
  return 'Invalid'

