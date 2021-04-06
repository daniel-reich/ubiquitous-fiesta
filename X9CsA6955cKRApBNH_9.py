
def longest_run(lst):
  B=sorted(lst)
  count=0
  C=[]
  for i in range(len(B)-1):
    if B[i]==B[i+1]:
      pass
    elif B[i]==B[i+1]-1:
      count+=1
      C.append(count)
    else:
      count=0
      C.append(0)
  return max(C)+1

