
def digital_vowel_ban(n, ban):
  al = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven']
  al.extend(['eight', 'nine'])
  ans, a10 = 0, 1
  boo = True
  while n > 0:
    t = al[n % 10]
    if ban not in t:
      ans = ans + (n % 10) * a10
      a10 = a10 * 10
      boo = False
    n = n // 10
  if boo:
    return 'Banned Number'
  return ans

