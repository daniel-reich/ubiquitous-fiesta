
def chunkify(lst, size):
    temp_lst = []
    lst2 = []
    a = len(lst)
    j = 0
  
    while j < a:
        temp_lst.append(lst[j])
        j += 1
        if j % size == 0:
            lst2.append(temp_lst)
            temp_lst = []
      
    if j % size != 0:
        lst2.append(temp_lst)
    return lst2

