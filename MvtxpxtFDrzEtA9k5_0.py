
def palindrome_descendant(num):
  num = str(num)
  while len(num) > 1:
    if num == num[::-1]:
      return True
    s = ""
    for idx in range(0, len(num), 2):
      try:
        s += str(int(num[idx]) + int(num[idx + 1]))
      except IndexError:
        pass
    num = s
  return False

