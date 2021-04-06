
def currently_winning(s):
  cys = [sum(s[:2*i+1:2]) for i in range(len(s) // 2)]
  cos = [sum(s[1:2*i:2]) for i in range(1,len(s) // 2+1)]
  return [[["O","Y"][y>o],"T"][y==o] for y,o in zip(cys,cos)]

