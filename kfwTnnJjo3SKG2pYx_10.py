
def replace_nums(txt):
  res = ''
  mini = []
  for i in range(len(txt)):
    item = txt[i]
    if not item.isnumeric() and not ('0' <= txt[i-1] and txt[i-1] <= '9'):
      res += item
    if item.isnumeric():
      mini.append(item)
    if not item.isnumeric() and '0' <= txt[i-1] and txt[i-1] <= '9':
      bn = bin(int(''.join(mini))).replace('0b', '')
      res += bn
      mini = []
      res += item
  return res

