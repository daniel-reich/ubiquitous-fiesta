
def wiggle_string(s):
  ans=[]
  for i in range(len(s)+1):
    ans.append(' '*i+s)
  for j in range((len(s)-1),-1,-1):
    ans.append(' '*j+s)
  return ans

