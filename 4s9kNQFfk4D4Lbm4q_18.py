
def ABA(s):
  str = ''
  for i in range(65,ord(s)+1):
    str += chr(i) + str
  return str

