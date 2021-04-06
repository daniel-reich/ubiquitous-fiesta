
def min_length(lst, n):
  successful_lst = []
  for num in range(len(lst)):
    print('>>>>>'+str(num))
    sum = 0
    num_nums = 0
    for i in range(num, len(lst)):
      if sum > n:
        print('appended', num_nums)
        successful_lst.append(num_nums)
        break
      sum += lst[i]
      print('here?')
      num_nums +=1
      if sum > n:
        print('appended', num_nums)
        successful_lst.append(num_nums)
        break
  print(successful_lst)
  if successful_lst == []:
    return -1
  smallest = successful_lst[0]
  for num in successful_lst:
    if smallest > num:
      smallest = num
  return smallest

