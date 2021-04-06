
def waterjug(start, goal):
  n=0;mem=[(0,0,start[-1]+0)];pool=[[0,0,start[-1]+0]]
  while mem:
    if goal in pool:return n
    n+=1;mem2=[]
    for i in mem:
      for j in range(3):
        if i[j]!=0:
          mem3=list(i)
          dif=min(start[(j+1)%3]-i[(j+1)%3],i[j])
          mem3[j]-=dif
          mem3[(j+1)%3]+=dif
          if not mem3 in mem2+pool:mem2+=[mem3]
          mem3=list(i)
          dif=min(start[(j-1)%3]-i[(j-1)%3],i[j])
          mem3[j]-=dif
          mem3[(j-1)%3]+=dif
          if not mem3 in mem2+pool:mem2+=[mem3]
    mem=[tuple(i) for i in mem2]
    pool+=mem2
  return "No solution."

