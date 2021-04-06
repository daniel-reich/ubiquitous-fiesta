
def palindrome_descendant(num):
  if num < 10:
    return False
  num = str(num)
  if len(num)&1:
    return False
  if num == num[::-1]:
    return True
  res = ''
  for i in range(0,len(num),2):
    res += str(int(num[i])+int(num[i+1]))
  return palindrome_descendant(int(res))

