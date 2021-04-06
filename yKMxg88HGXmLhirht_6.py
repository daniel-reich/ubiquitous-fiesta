
def add_letters(a):
  k=ord('a')
  if a:
    s=sum(ord(x)-k+1 for x in a)%26
    return chr(s+k-1) if s else 'z'
  else:
    return 'z'

