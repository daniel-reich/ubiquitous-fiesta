
def validate_binary(b):
  length = len(b)
  i1 = 0
  for i in range (length):
    if b[i] == '1':
      i1 += 1
  if(i1 % 2 == 1):
    return False
  
  return True

