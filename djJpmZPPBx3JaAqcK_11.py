
def maya_number(n):
  ls = ["@","o", "oo", "ooo", "oooo", "-", "o-", "oo-", "ooo-", "oooo-", 
  "--", "o--", "oo--", "ooo--", "oooo--", "---", "o---", "oo---",
  "ooo---", "oooo---"]
  res = []
  if n % 20 == 0 and n > 20:
    res.append(ls[0])
  while n % 20 != 0 or n // 20 > 20:
    if n % 20 != 0:
      res.insert(0,ls[n % 20])
      n -= n % 20
    elif n % 20 == 0 and (n // 20) % 20 == 0:
      res.insert(0,ls[0])
      n = n // 20
    elif n % 20 == 0 and (n // 20) % 20 != 0:
      n = n // 20
      res.insert(0, ls[n % 20])
      n -= n % 20
  res.insert(0,ls[n // 20])
  return res

