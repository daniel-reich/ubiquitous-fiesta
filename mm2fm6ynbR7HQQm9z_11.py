
def knights_jump(square):
  x=ord(square[0])-ord('A')
  y=int(square[1])
  
  out=[]
  for b,a in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
    if a+x>=0 and b+y>0 and a+x<8 and b+y<=8:
      out.append(chr(x+a+ord('A'))+str(y+b))
  print(out)
  return ','.join(out)

