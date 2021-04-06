
def is_early_bird(_range, n):
  s = ''.join([str(i) for i in range(_range+1)])
  n = str(n)
  lst = []
  for i in range(len(s)-len(n)+1):
    temp = []
    if s[i] == n[0]:
      for x in range(len(n)):
        if s[i+x]==n[x]:
          temp.append(i+x)
    if len(temp) == len(n):
      lst.append(temp)
  if len(lst)>1:
    lst.append('Early Bird!')
  return lst

