
def ABA(s):
  if s == 'A': return s
  return '{0}{1}{0}'.format(ABA(chr(ord(s)-1)), s)

