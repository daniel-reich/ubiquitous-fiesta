
def number_len_sort(lst):
  output = []
  for nums in lst:
    if len(str(nums)) == 1:
      output.append(nums)
  for nums in lst:
    if len(str(nums)) == 2:
      output.append(nums)
  for nums in lst:
    if len(str(nums)) == 3:
      output.append(nums)
  for nums in lst:
    if len(str(nums)) == 4:
      output.append(nums)
  return output

