
def can_capture(queens):
  row = "ABCDEFGH"
  col = "12345678"
  diags = []  
  Q = [i.translate(i.maketrans(row,col)) for i in queens]
  a1,a2,b1,b2 =int(Q[0][0]),int(Q[0][1]),int(Q[1][0]),int(Q[1][1]),
  if a2==b2 or a1==b1:
    return True
  elif abs(a1-b1)==abs(a2-b2):
    return True 
  return False

