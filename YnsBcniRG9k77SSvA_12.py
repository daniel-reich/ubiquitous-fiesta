
def print_all_groups():
  nums = "123456"
  chars = "abcde"
  retlist = []
  for num in nums:
    for char in chars:
      retlist.append(num + char)
  retstr = ', '.join(retlist)
  print(retstr)
  return (retstr)

