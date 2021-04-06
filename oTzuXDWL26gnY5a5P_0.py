
def prime_numbers(num):
  return sum(1 for i in range(2,int(num)) if all(i%j for j in range(2,i)))

