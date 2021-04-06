
def next_prime(num):
  for i in range(2,num):
    print(num,i)
    if i == num-1:
      return num
    if num%i == 0:
      return next_prime(num+1)

