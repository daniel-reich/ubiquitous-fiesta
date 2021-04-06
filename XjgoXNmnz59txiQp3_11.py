
def split(number):
  lst = []
  lst.append(0);
  lst.append(1);
  for i in range(2,number+1):
    m = i;
    for j in range(1,i):
      if (lst[j] * lst[i-j]) > m:
        m = lst[j] * lst[i-j];
    lst.append(m);
  return lst[number]

