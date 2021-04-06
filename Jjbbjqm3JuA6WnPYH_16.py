
def bit_rotate(n, m, d):
  bin = format(n,"b")
  one = []
  for i in range(len(bin)):
    if bin[i]=='1':
      one.append(i)
  
  if d==True:
    for i in range(len(one)):
      if one[i]+m > (len(bin)-1):
        tmp = (m-(len(bin)-1-one[i]))%len(bin)
        if tmp == 0:
          one[i] = len(bin)-1
        else:
          one[i] = tmp-1
      else :
        one[i] = one[i]+m
  else:
    for i in range(len(one)):
      if one[i]-m < 0:
        tmp = (m-one[i])%len(bin)
        if tmp == 0:
          one[i] = 0
        else:
          one[i] = len(bin)-tmp
      else :
        one[i] = one[i]-m
​
  sum = 0
  for i in range(len(bin)):
    for j in one:
      if i == len(bin)-j-1:
        sum += 2**i
  return sum

