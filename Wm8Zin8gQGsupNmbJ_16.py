
def binary_conversion(txt):
  lst = []
  result = ""
  for i in range(1, len(txt)):
    if i % 8 == 0:
      lst.append(txt[i-8: i])
    if i == len(txt) - 1:
      lst.append(txt[len(txt) - 8:])
  for i in lst:
    result += chr(int(i, 2))
  return result

