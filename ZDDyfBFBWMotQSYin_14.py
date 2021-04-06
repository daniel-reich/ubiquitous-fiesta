
def is_harshad(num):
  total = [int(str(num)[i]) for i in range(len(str(num)))]
  total = sum(total)
  if total == 0:
    return False
  if num % total == 0:
    return True
  else:
    return False

