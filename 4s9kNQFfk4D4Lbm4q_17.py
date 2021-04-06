
def ABA(s):
  if s == 'A':
    return 'A'
  else:
    use = chr(ord(s)-1)
    return ABA(use) + s + ABA(use)

