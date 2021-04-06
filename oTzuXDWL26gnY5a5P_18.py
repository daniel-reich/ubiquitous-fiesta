
def prime_numbers(num):
  count=0
  for num in range(num):
    if num > 1:
      for i in range(2, num):
        if (num % i) == 0:
          break
      else:
        count=count+1
  return count

