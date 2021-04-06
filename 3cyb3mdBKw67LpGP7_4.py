
def numbers_need_friends_too(n):
  s = str(n)
  groups = []
  cur = ''
  for i in s:
    if i in cur or cur=='':
      cur+=i
    else:
      groups.append(cur)
      cur = i
  if cur!='':
    groups.append(cur)
​
  for i in range(len(groups)):
    if len(groups[i])==1:
      groups[i] = groups[i].replace(groups[i][0],groups[i][0]*3,1)
  return int(''.join(groups))

