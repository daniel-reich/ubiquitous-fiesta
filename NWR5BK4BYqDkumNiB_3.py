
def digital_division(n):
  res = 0
  flag=0
  product = 1
  for i in str(n):
    if int(i)!=0:
      if n%int(i) != 0:
        flag=1
        break
  if flag == 0: res+=1
  if n%sum(int(j) for j in str(n)) == 0: res+=1
  if str(n).count("0") == 0:
    for i in str(n):
      product*=int(i)
    if n%product == 0: res+=1
​
  if res == 3: return "Perfect"
  elif res == 0: return "Indivisible"
  else: return res

