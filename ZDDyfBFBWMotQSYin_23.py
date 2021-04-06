
def is_harshad(num):
  return not num%sum(int(i) for i in str(num)) if num != 0 else False

