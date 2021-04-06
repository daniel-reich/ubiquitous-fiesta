
def palindrome_descendant(num):
  s_num = str(num)
  l = len(s_num)
  if s_num == s_num[::-1]:
    return True
  if l == 2:
    return False
  if (l % 2) != 0:
    s_num += '0'
  new_num = ''
  while l > 0:
    new_num += str(int(s_num[0]) + int(s_num[1]))
    s_num = s_num[2:]
    l -= 2
  return palindrome_descendant(new_num)

