
def is_positive_dominant(lst):
  p_list,n_list = [],[]
​
  for x in lst:
    if (x < 0) and (x not in n_list): n_list.append(x)
    elif (x > 0) and (x not in p_list): p_list.append(x)
  
  return len(p_list) > len(n_list)

