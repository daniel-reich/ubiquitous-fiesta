
def maxmin(n):
  lst = [n]
  n = str(n)
  for i in range(len(n)):
    for j in range(i+1,len(n)):
      temp = list(n)
      temp[i],temp[j] = temp[j],temp[i]
      if temp[0]!='0' and int(''.join(temp)) not in lst:
        lst.append(int(''.join(temp)))
  return (max(lst),min(lst))

