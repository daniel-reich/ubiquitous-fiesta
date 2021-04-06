
def palindrome_descendant(num):
  def is_palin(num): return all([str(num)[i] == str(num)[-i - 1] for i in range(int(len(str(num)) / 2))])
  num = str(num)
  while len(num) >= 2:
    if is_palin(int(num)):
      return True
    if len(num) % 2 == 1 or len(num) == 2:
      break
    new_num = ''
    for i in range(1, len(num), 2):
      new_num += str(int(num[i]) + int(num[i - 1]))
    num = new_num
  return False

