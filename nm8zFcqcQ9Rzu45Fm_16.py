
def bridge_shuffle(lst1, lst2):
  result = [];
  rev_lst1 , rev_lst2 = lst1[::-1] , lst2[::-1];
  while (len(rev_lst1) > 0 and len(rev_lst2) > 0):
    result.append(rev_lst1.pop());
    result.append(rev_lst2.pop());
  return (result + rev_lst1 + rev_lst2);

