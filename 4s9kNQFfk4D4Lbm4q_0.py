
def ABA(s):
  res = ''
  for i in range(ord('A'), ord(s)+1):
    res = res + chr(i) + res
  return res

