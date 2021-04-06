
import itertools
def ulam(n):
  lst = [1, 2]
  if n == 1:
    return 1
  elif n == 2:
    return 2
  else:
    j = 3
    for i in range(3, n + 1,1):
      lop = [x for x in itertools.combinations(lst,2)]
      flag = True
      while flag:
        count = 0
        for x in lop:
          if sum(x) == j:
            count += 1
          if count > 1:
            break
        if count == 1:
          #print('j=', j, '-->', count)
          lst.append(j)
          flag = False
        j += 1
        print(lst)
    return lst[n - 1]

