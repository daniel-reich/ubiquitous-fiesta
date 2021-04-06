
def show_the_love(lst):
  new_lst=[0.75*i for i in lst]
  reduced=sum([0.25*i for i in lst])
  final_list=[]
  for i in new_lst:
    if i==min(new_lst):
      final_list.append(i+reduced)
    else:
      final_list.append(i)
  return final_list

