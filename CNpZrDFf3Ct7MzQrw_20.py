
def trouble(num1, num2):
  lst_num_strs = []
  for i in str(num1):
    lst_num_strs.append(i)
  unique_nums = list(set(lst_num_strs))
  unique_nums_tripled = []
  for num in unique_nums:
    unique_nums_tripled.append(num * 3)
  triple_num = ""
  double_num = ""
  for num in unique_nums_tripled:
    if num in str(num1):
      triple_num += num
      double_num = triple_num[0] + triple_num[1]
      if double_num in str(num2):
        return True
  return False

