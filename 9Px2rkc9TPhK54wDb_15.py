
def ecg_seq_index(n):
  lst = [1, 2]
  while not n in lst:
    appended = False
    for i in range(3, 1000):
      if i in lst:
        pass
      else:
        lst_factors = [x for x in range(2, lst[-1]+1) if lst[-1] % x == 0]
        i_factors = [x for x in range(2, i+1) if i % x == 0]
        for j in i_factors:
          if j in lst_factors:
            lst.append(i)
            appended = True
            break
      if appended:
        break
  return lst.index(n)

