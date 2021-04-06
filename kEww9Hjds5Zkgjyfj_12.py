
def replace_next_largest(lst):
  test = sorted(lst)
  output = []
  for i in lst:
    if i == max(lst):
      output.append(-1)
    else:
      output.append(test[test.index(i)+1])
  return output

