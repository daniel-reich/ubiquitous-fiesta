
def ABA(s):
  if s=='A':
    return 'A'
  else:
    return ABA(chr(ord(s)-1))+s+ABA(chr(ord(s)-1))

