
def count_substring(s):
  As_up_to_i = 0
  total_up_to_i = 0
  for i in s:
    if i == "A": As_up_to_i += 1
    if i == "X": total_up_to_i += As_up_to_i
  return total_up_to_i

