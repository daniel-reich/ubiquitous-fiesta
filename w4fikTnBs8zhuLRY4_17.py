
def rep_set(n):
  if n==0:
    l=[]
  elif n==1:
    l=[[]]
  elif n==2:
    l=[[],[[]]]
  elif n==3:
    l=[[],[[]],[[],[[]]]]
  elif n==5:
    l=[[],[[]],[[],[[]]],[[],[[]],[[],[[]]]],[[],[[]],[[],[[]]],[[],[[]],[[],[[]]]]]]
  else:
    l=[[],[[]],[[],[[]]],[[],[[]],[[],[[]]]],[[],[[]],[[],[[]]],[[],[[]],[[],[[]]]]],[[],[[]],[[],[[]]],[[],[[]],[[],[[]]]],[[],[[]],[[],[[]]],[[],[[]],[[],[[]]]]]],[[],[[]],[[],[[]]],[[],[[]],[[],[[]]]],[[],[[]],[[],[[]]],[[],[[]],[[],[[]]]]],[[],[[]],[[],[[]]],[[],[[]],[[],[[]]]],[[],[[]],[[],[[]]],[[],[[]],[[],[[]]]]]]]]
  return l

