
def split_into_buckets(phrase, n):
  ans=[]
  while phrase.strip()!='':
    found=False
    if len(phrase)<=n:
      ans.append(phrase.lstrip())
      return ans
    for a in range(n-1,-1,-1):
      if phrase[a]==' ' or phrase[a+1]==' ':
        found=True
        ans.append(phrase[0:a+1].rstrip())
        phrase=phrase[a+1:].lstrip()
        print(ans,phrase)
        break
    if found==False:
      return []
  return ans
print(split_into_buckets("a b c d e", 2))

