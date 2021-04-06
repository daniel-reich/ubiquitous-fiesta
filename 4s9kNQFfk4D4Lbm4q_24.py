
def ABA(s):
  return 'A' if s is 'A' else ABA(chr(ord(s) - 1)) + s + ABA(chr(ord(s) - 1))

