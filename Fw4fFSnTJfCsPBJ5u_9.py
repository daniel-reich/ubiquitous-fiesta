
def how_many_missing(lst):
  miss=0
  for i in range (len(lst)-1):
    while lst[i+1]!=lst[i]+1:
      lst[i]+=1
      miss+=1
  return miss

