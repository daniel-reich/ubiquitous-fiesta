
def lcm_of_list(numbers):
  for i in range(len(numbers)-1):
    numbers[i+1]=int(lcm(numbers[i],numbers[i+1]))
  return numbers[len(numbers)-1]
def lcm(i,j):
  return i*j/gcd(i,j)
def gcd(i,j):
  m=1
  for k in range(1,i):
    if((i%k==0) & (j%k==0)):
      m=k
  return int(m)

