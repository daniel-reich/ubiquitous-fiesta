
def repeated(s):
  return not all([s != s[0:i]*int(len(s)/i) for i in range(1, int(len(s)/2)+1) if len(s)%i == 0])

