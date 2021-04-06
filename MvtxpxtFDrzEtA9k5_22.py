
def isPalindrom(n):
  for i in range(len(str(n)) // 2 + 1):
    if str(n)[i] != str(n)[-(i + 1)]:
      return False
  return True
  
def palindrome_descendant(num):
  if isPalindrom(num):
    return True
  else:
    next_n = ""
    number = [int(d) for d in str(num)]
    for i in range(0, len(number) - 1, 2):
      next_n += str(sum(number[i: i + 2]))
    if int(next_n) // 10 == 0:
      return isPalindrom(num)
    else:
      return palindrome_descendant(int(next_n))

