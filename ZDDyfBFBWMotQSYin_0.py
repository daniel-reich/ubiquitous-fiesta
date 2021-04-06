
def is_harshad(num):
  return num!= 0 and num % sum(int(x) for x in str(num)) == 0

