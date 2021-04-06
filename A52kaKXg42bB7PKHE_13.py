
def num_then_char(lst):
  all_st=[item for list_item in lst for item in list_item if type(item) == str]
  all_num=[item for list_item in lst for item in list_item if not type(item) == str]
  all_st.sort()
  all_num.sort()
  
  counter=0
  for index,litem in enumerate(lst):
    for index_ll,ll in enumerate(litem):
      if counter<len(all_num):
        lst[index][index_ll]=all_num[counter]
      else:
        lst[index][index_ll]=all_st[counter - len(all_num)]
      counter+=1
  return(lst)

