
def create_square(length):
  if length == None or length < 1: return ""
  if length == 1: return "#"
  square = '#' * length + "\n"
  for x in range(1, length - 1):
    square += "#" + (" " * (length - 2)) + "#\n"
  square += "#" * length
  return square

