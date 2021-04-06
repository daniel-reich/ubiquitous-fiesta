
def reverse_and_not(i):
  string_i = str(i)
  reverse_i = reversed(string_i)
  joined_i = "".join(reverse_i)
  return int(joined_i + string_i)

