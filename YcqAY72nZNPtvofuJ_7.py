
def quad_sequence(lst):
  last_diff = lst[-1] - lst[-2]
  diff_diff = last_diff - (lst[-2] - lst[-3])
  last_num = lst[-1]
  output = []
  for i in range(len(lst)):
    last_diff += diff_diff
    last_num = last_num + last_diff
    output.append(last_num)
  return output

