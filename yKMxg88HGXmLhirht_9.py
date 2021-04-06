
def add_letters(a):
  a=sum([ord(i)-96 for i in a])
  while a>26:
    a-=26
  if a==0: return 'z'
  return chr(a+96)

