
def ABA(s):
  cur,p = 'B',['A']
  while cur<=s:
    p += [cur]+p[::-1]
    cur = chr(ord(cur)+1)
  return ''.join(p)

