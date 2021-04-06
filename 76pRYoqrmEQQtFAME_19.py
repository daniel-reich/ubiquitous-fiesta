
def is_astonishing(num):
  for i in range(1,len(str(num))):
    a,b=int(str(num)[:i]),int(str(num)[i:])
    low=(-1)**(b<=a)
    if low<0: a,b=b,a
    r=(a+b)*(b-a+1)//2
    if r==num: return "AB"[::low]+"-Astonishing"
  return False

