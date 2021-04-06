
def is_harshad(num):
  x= sum([int(i) for i in str(num)])
  if num == 0: return False
  if num%x == 0: return True
  return False

