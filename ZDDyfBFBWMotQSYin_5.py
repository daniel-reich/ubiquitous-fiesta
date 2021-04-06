
def is_harshad(num):
  return num and not num%sum(int(i) for i in str(num))

