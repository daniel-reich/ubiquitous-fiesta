
def divide(lst, the_sum):
  result , current  = [] , [];
  for idx in range(0 , len(lst)):
    elem = lst[idx];
    if (sum(current) +  elem  > the_sum):
      result.append(current[:]);
      current = [elem];
    else :
      current.append(elem);
  result.append(current[:]);
  return result;

