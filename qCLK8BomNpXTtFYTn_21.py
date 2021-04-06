
def cumulative_sum(lst):
  out=[]
  for i in range(len(lst)):
    if i == 0: out.append(lst[i])
    else: out.append(lst[i]+out[i-1])
    
  return out

