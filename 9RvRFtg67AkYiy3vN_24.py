
def left_rotations(txt):
  t_str = txt
  t_list= []
  for i in range(len(txt)):
    t_list.append(t_str)
    t_str = t_str + t_str[0]
    t_str = t_str[1:]
  return t_list
​
​
def right_rotations(txt):
  t_str = txt
  t_list= []
  for i in range(len(txt)):
    t_list.append(t_str)
    t_str = t_str[-1] + t_str 
    t_str = t_str[:-1]
  return t_list

