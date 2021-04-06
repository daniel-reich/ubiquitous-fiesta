
def invert(s):
  final_string = ''
  for values in s[::-1]:
    final_string += values.swapcase()
  return final_string

