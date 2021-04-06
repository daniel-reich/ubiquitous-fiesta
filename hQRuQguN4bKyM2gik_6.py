
def simple_check(a, b):
    cnt = 0
    c = a
    d = b
    while min(c,d)>0:
      if max(c,d)%min(c,d) == 0:
            cnt+=1
      c =c-1
      d=d-1
      
    return cnt
print(simple_check(10,1))

