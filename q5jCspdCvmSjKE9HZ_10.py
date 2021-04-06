
def lcm(a,b):
  if a<b:
    a,b=b,a
  for i in range(b,a*b+1):
    if i%a==0 and i%b==0:
      break
  return i
def lcm_of_list(numbers):
  m=lcm(numbers[0],numbers[1])
  for i in range(2,len(numbers)):
    m=lcm(m,numbers[i])
  return m

