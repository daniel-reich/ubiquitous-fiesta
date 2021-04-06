
def check_perfect(num):
  return sum([i for i in list(range(1,num)) if num%i==0])==num

