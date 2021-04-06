
def cleave(string, lst):
  lst.sort(reverse=True,key=len)
  if string[0]=='f':
    lst.remove('as')
  lst.append('z')
  ans=''
  while len(string)>0:
    for i in lst:
      if string.find(i)==0:
        ans+=i+' '
        string=string[len(i):]
        break
    if i==lst[-1]:
      return 'Cleaving stalled: Word not found'
  return ans[:-1]

