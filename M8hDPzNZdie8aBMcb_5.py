
def count_substring(s):
  indices_A = []
  length_A = 0
  indices_X = []
  length_X = 0
  index = 0
  for char in s:
    if char == "A":
      indices_A.append(index)
      length_A += 1
    elif char == "X":
      indices_X.append(index)
      length_X += 1
    index += 1
  index = 0
  ind_A = 0
  count = 0
  copy_length = length_X
  while index < length_X and ind_A < length_A:
    if indices_A[ind_A] > indices_X[index]:
      index += 1
      copy_length -= 1
    else:
      count += copy_length
      ind_A += 1
  return count

