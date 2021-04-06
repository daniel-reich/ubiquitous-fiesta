
def even_odd_transform(lst, n):
  return_list = lst
  for i in range(n):
    for index, number in enumerate(lst):
      if number % 2 == 0:
        return_list[index] = number - 2
      else:
        return_list[index] = number + 2
  return return_list

