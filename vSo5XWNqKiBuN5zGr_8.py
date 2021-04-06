
def divide(x, y, s=None, d=0):
     if not s: s=(x//abs(x))*(y//abs(y)) if x else 1
     return divide(x-s*y,y,s,d+1) if(x-s*y)*x>0 else s*d if x-s*y else s*(d+1)

