
def cpp_txt(lst):
  lst.remove(lst[-1])
  word = ''
  for i in lst:
    word += i
  return word

