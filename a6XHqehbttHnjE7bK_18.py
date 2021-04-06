
def is_repdigit(num):
  for i in range(len(str(num)) - 1):
    if str(num)[i] != str(num)[i + 1]:
      return False
  if num == 0:
    return True
  if num < 0:
    return False
  else:
    return True

