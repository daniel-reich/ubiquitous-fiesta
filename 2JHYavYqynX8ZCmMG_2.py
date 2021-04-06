
def ascii_sort(lst):
  return min([(sum([ord(char) for char in word]),word) for word in lst])[1]

