
prime = []
for i in range(2,10000):
  b = 0
  for j in range(2,100):
    if j**2<=i:
      if i%j==0:
        b+=1
  if b==0:
    prime.append(i)
def express_factors(n):
    ans = []
    k = 0
    if n not in prime:
        for i in prime:
            for j in range(1,15):
                if n%(i**j)==0:
                    if j==1:
                        k = i
                    else:
                        k = str(str(i) + '^' + str(j))
            if k!=0 and k not in ans:
                ans.append(k)
    else:
        ans.append(n)
    d = str()
    for i in ans:
        if i==ans[0]:
            d = str(i)
        else:
            d = d + ' x ' + str(i)
    return d

