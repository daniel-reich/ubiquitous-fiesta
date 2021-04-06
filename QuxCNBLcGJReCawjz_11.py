
def palindrome_type(n):
  
  lst = [int(i) for i in list(str(n))]
  decimal = True
  while len(lst) > 1:
    if lst[0] != lst[-1]:
      decimal = False
      break
    lst.pop(0)
    lst.pop(-1)
    
  lst = list(bin(n))
  lst.pop(0)
  lst.pop(0)
  lst = [int(i) for i in lst]
  binary = True
  while len(lst) > 1:
    if lst[0] != lst[-1]:
      binary = False
    lst.pop(0)
    lst.pop(-1)
    
  if decimal and binary:
    return 'Decimal and binary.'
  elif decimal:
    return 'Decimal only.'
  elif binary:
    return 'Binary only.'
  else:
    return 'Neither!'

