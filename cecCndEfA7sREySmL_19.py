
def challenge1(s):
  return s[0:5]
  
def challenge2(s):
  return s[-5::]
  
def challenge3(s):
  return s[::-1]
  
def challenge4(s):
  return s[0:6][::-1]
  
def challenge5(s):
  a = (s[-7],s[-5],s[-3],s[-1])
  return ''.join(i for i in a)

