
def prime_numbers(num):
  if num <= 1:
    return 0
  
  else:
    count = 1
    for i in range(3,num):
      l = []
      for j in range(2,i):
        l.append(i%j)
      if l.count(0) == 0:
        count += 1
    return count

