
def diamond_sum(n):
  cnt=1
  res=[]
  temp=[]
  sums=[]
  for i in range(n):
      for j in range(cnt,cnt+n):
          temp.append(j)
      res.append(temp)
      if i<= n//2:
          sums.append(temp[(n//2)-i])
          sums.append(temp[-((n//2)-i)-1])
          temp=[]
          cnt+=n
      else:
          sums.append(temp[-((n//2)-i)])
          sums.append(temp[((n//2)-i)-1])
          temp=[]
          cnt+=n
  return sum(set(sums))

