
def is_kaprekar(n):
  sq = n**2
  a = 0
  b = 0
  if len(str(sq)) % 2 == 0:
    #even
    a = str(sq)[0:int(len(str(sq))/2)]
    b = str(sq)[int(len(str(sq))/2):]
    if int(a) + int(b) == n:
      return True
  else :
    #odd
    if len(str(sq)) > 2:
      a = str(sq)[0:int(len(str(sq))/2)]
      b = str(sq)[int(len(str(sq))/2):]
      if int(a) + int(b) == n:
        return True
    else : return sq == n
    
    
  print(a)
  print(b)
  return False

