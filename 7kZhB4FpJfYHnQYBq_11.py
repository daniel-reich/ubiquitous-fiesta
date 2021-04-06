
def lcm_three(num):
  a=num[0]
  b=num[1]
  c=num[2]
  temp=b
  while True:
    if b%a==0:
      temp=c
      while True:
        if c%b==0:
          return c
        else:
          c+=temp
    else:
      b+=temp

