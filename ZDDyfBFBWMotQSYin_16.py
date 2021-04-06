
def is_harshad(num):
  return False if num == 0 else num % (sum(int(d) for d in str(num))) == 0

