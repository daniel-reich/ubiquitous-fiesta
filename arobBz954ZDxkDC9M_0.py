
def next_prime(num):
  while [i for i in range(2, num) if num%i==0]:
    num+=1
  return num

