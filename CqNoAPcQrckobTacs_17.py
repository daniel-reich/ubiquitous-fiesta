
def missing_letter(lst):
  for i in map(chr,range(ord(lst[0]),ord(lst[-1]))):
    if i not in lst:return i

