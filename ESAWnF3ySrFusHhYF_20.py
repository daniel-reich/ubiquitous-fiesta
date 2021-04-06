
def edit_words(lst):
  ans=[]
  for i in lst:
    a=[]
    if i=='':ans.append('-')
    else:
      for j in range(len(i)-1,-1,-1):
        if j==len(i)//2:
          a.append(i[j].upper())
          a.append('-')
        else:a.append(i[j].upper())
      ans.append(''.join(a))
  return ans

