
def expanded_form(num):
  list_num = [int(i) for i in list(str(num))]
  mult_list_num = []
  index = 0  
  for i in list_num:
    mult_list_num.append(i*10**((len(list_num)-1-index)))
    index = index +1
  return ' + '.join( [str(i) for i in [i for i in mult_list_num if i != 0]] )

