
def ABA(s):
  return 'A' if s=='A' else ABA(chr(ord(s)-1))+s+ABA(chr(ord(s)-1))

