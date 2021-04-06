
def big_sub(lst):
  #print(lst)
  max,out,last=-999,[],-999
  for i,x in enumerate(lst):
    tmp=0
    if x>0 and last<0:
      for j in range(len(lst)-i):
       tmp+=lst[i+j] #sum(lst[i:i+j+1])
       if tmp>=max:max,out=tmp,[i,i+j]
    last=x
    
  return [max]+out

