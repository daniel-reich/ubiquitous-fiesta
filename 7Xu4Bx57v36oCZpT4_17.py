
def where_is_waldo(lst):
  x_pos = 1
  for each_lst in lst:
      set_each = list(set(each_lst))
      if len(set_each) !=1 :
          odd_ele = set_each[0] if each_lst.count(set_each[0]) == 1 else set_each[1]
          y_pos = each_lst.index(odd_ele)+1
          break
      x_pos+=1
  return [x_pos, y_pos]

