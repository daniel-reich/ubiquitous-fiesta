
def cycle_length(lst, n):
  lst_s = sorted(lst);
  index = lst.index(n);
  index_s = lst_s.index(n);
  if (index == index_s):
    return 0;
  count = 0;
  while (1):
    temp = lst[index_s]
    lst[index_s] = lst[index]
    lst[index] = temp
    count += 1;
    index_s = lst_s.index(temp);
    if (index == index_s):
      return count;

