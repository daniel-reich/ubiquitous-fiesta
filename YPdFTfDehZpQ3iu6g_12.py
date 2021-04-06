
def rton(r):
  l1 = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5}
  l2 = {'CM': 900, 'XC': 90, 'IX': 9, 'CD': 400, 'XL': 40, 'IV': 4}
  ans = 0
  while len(r) > 0:
    try: 
      ans += l2[r[:2]]
      r = r[2:]
    except:
      try:
        ans += l1[r[0]]
        r = r[1:]
      except: return ans + len(r)
  return ans
​
def ntor(n):
  l1 = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
  l2 = {'CM': 900, 'XC': 90, 'IX': 9, 'CD': 400, 'XL': 40, 'IV': 4}
  l1.update(l2)
  l = {k: v for v, k in l1.items()}
  ans = ''
  for i in sorted(l.keys(), reverse=True):
    while n - i >= 0:
      ans += l[i]
      n -= i
  return ans
​
def roman_numerals(arg):
  return rton(arg) if type(arg) is str else ntor(arg)

