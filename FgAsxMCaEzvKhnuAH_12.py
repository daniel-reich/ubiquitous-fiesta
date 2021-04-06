
def deep_sum(lst):
  def flatten_matrix(input_matrix):
    output = []
    for i in input_matrix:
      if type(i) != list:
        output.append(i)
      else:
        output += flatten_matrix(i)
    return output
  lst = flatten_matrix(lst)
  total = 0
  for i in lst:
    current_num = "0"
    for j in i:
      if j in "0123456789":
        current_num += j
      elif j == "-":
        total += int(current_num)
        current_num = "-0"
      else:
        total += int(current_num)
        current_num = "0"
    total += int(current_num)
  return total

