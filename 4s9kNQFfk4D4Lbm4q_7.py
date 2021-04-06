
def ABA(s):
  alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  index_s = alphabets.index(s)
  n = ''
  u = ''
  if s == 'A':
    return s
  else:
    for i in range(index_s+1):
      if alphabets[i] == 'A':
        n = 'A'
      else:
        u = n[:]
        n = n[:] + alphabets[i] + u
    return n

