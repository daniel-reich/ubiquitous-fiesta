
def clean_up_list(lst):
  answ_lst = [[],[]]
  for num in lst:
    num = int(num)
    if num % 2 == 0:
      answ_lst[0].append(num)
    elif num % 2 != 0:
      answ_lst[1].append(num)
  return answ_lst

