
def sum_of_slices(lst):
  result_lst = [];
  current_sum = 0;
  for num in lst :
    if (current_sum + num  < 100):
      current_sum += num;
    else :
      result_lst .append(current_sum);
      current_sum  =  num;
  result_lst.append(current_sum);
  return result_lst;

