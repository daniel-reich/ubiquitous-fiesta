
def check_perfect(num):
  factors = [i for i in range(1,num//2+1) if num % i == 0]
  return sum(factors) == num

