
def add(n1, n2):
  if (n1 == ''  or n1 == None) or (n2 == '' or n2 == None):
    return 'Invalid Operation'
  return str(eval('{}+{}'.format(n1 , n2)))

