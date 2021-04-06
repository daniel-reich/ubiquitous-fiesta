
L = list("IVXLCDM")
N = [1, 5, 10, 50, 100, 500, 1000]
R = dict(zip(L, N))
​
def roman_numerals(s):
  if isinstance(s, int): return num_to_roman(s)
  res = 0
  for i, x in enumerate(s):
    res += R[x] if i == len(s) - 1 or R[x] >= R[s[i + 1]] else -R[x]
  return res
​
def num_to_roman(n):
  res = ""
  while n > 0:
    l, v = next((_, x) for _, x in list(zip(L, N))[::-1] if n >= x)
    res += l
    n -= v
  return res.replace("IIII", "IV")

