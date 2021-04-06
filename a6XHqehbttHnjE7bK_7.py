
def is_repdigit(num):
  if num < 0: return False
  if num == 0: return True
  return sum([int(i) for i in str(num)]) == len(str(num)) * int(str(num)[0])

