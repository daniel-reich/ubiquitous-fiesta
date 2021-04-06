
def parity_analysis(num):
  tmp = 0
  for i in str(num): tmp+=int(i)
  if num%2 == tmp%2: return True
  return False

