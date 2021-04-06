
def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
def ecg_seq_index(n):
  res, l, s, b = [1, 2], 2, 3, {}
  for _ in range(1000):
    i = s
    while True:
      if not i in b and gcd(i, l) > 1:
        res.append(i)
        l, b[i] = i, True
        while s in b:
          b.pop(s)
          s += 1
        break
      i+=1
  return res.index(n)

