
def is_harshad(num):
  return False if sum([int(x) for x in str(num)])==0 else num%sum([int(x) for x in str(num)])==0

