
def bit_rotate(n, m, d):
  s = list(bin(n)[2:])
  for i in range(m):
    s.insert(0, s.pop()) if d else s.append(s.pop(0))
​
  return int(''.join(s), 2)

