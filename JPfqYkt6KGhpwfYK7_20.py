
def replace_the(txt):
  txt=txt.split()
  ans=[]
  for i in range(len(txt)):
    if txt[i]=='the':
      if txt[i+1][0] in 'aeiou':
        ans.append('an')
      else: ans.append('a')
    else: ans.append(txt[i])
  return ' '.join(ans)

