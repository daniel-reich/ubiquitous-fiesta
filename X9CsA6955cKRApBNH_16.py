
def longest_run(lst):
  cnt=1
  cnt2=1
  tl=[1]
  for i in range(1,len(lst)):
    if (lst[i-1]==lst[i]+1):
      cnt+=1
      tl.append(cnt)
    elif(lst[i-1]==lst[i]-1):
      cnt2+=1
      tl.append(cnt2)
    else:
      cnt=1
      cnt2=1
    
  return  max(tl)

