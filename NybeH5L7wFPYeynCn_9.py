
def three_letter_collection(s):
  ans=[]
  for i in range(len(s)-2):
    ans.append(s[i:i+3])
  return sorted(ans)

