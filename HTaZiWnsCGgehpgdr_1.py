
def license_plate(s, n):
  tmp = [i.upper() for i in s if i != '-']
  if n == 2 or 3 or 4:
    indx = n 
    while indx < len(tmp):
      tmp.insert((len(tmp) - indx), '-')
      indx += (n + 1)
    return ''.join(tmp)
  else:
    return s

