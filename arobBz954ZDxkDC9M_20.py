
def next_prime(num):
  while True:
    for i in range(2, int(num/2)+1):
      if num%i == 0:
        break
    else:
      return num
    num += 1

