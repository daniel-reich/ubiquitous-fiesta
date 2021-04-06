
def boxes(weights):
    a=0;box=0
    for i in range(1,len(weights)+1):
      w=sum(weights[a:i])
      if w>=10:
        box+=1
        a=i-(w>10)
    if 10>w>0 or a==len(weights)-1:
      box+=1
    return box

