
def is_harshad(num):
  return num%sum([int(i) for i in str(num)]) == 0 if num!= 0 else False

