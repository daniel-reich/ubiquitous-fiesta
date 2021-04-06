
def simple_check(a, b):
  count=0
  while True:
    if (max(a,b)/min(a,b))%1==0:count+=1
    a=a-1
    b=b-1
    if a==0 or b==0:return count

