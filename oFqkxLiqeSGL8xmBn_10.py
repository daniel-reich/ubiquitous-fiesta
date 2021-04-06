
def add_two_numbers(l1, l2):
  a,b= l1.get_data(), l2.get_data()
  over=0
  out=[]
  for x,y in zip( a + [0]*(2+ abs(len(a)-len(b)) ) , b + [0]*(2+ abs(len(a)-len(b)) ) ):
    over+=x+y
    out.append(over%10)
    over=(over-over%10)//10
​
  while len(out)>1 and out[-1]==0:
    out=out[:-1]
​
  lsum=ListNode(out[0])
  lsum.add_data(out[1:])
  return lsum

