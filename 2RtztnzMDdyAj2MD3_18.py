
def add(n1, n2):
  if n1 == '' or n2 == '' or n1 == None or n2 == None:
    return 'Invalid Operation'
  else:
    return str(eval(n1 + '+' + n2))

