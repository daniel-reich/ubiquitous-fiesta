
def is_zygodrome(num):
  #return len(set(str(num))) <= len(str(num))/2
  num = str(num)
  if len(num)<2:
    return False
  if num[0] != num[1] or num[-1] != num[-2]:
    return False
  for i in range(1, len(num) - 1):
    if num[i] != num[i+1] and num[i] != num[i-1]:
      return False
  return True

