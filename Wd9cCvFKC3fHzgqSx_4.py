
def num_split(num):
  n = str(abs(num))
  c = 0
  c2 = len(n)
  lst = [i for i in n]
  lst2 = []
  while len(lst2)<len(n):
    lst2.append(lst[c]+'0'*(c2-1))
    c+=1
    c2-=1
  return [-int(i) if num<0 else int(i) for i in lst2]

