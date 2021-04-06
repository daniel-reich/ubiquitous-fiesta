
def next_prime(num):
  flag = 0
  while True:
    for i in range(2,num):
      if num % i == 0:
        flag += 1
    if flag == 0:
      return num
    flag = 0
    num += 1

