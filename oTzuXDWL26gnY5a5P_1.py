
def prime_numbers(num):
  return sum(all(i%x for x in range(2,i)) for i in range(2,num))

