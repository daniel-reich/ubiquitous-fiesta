
def is_polygonal(n):
  result = []
  num = lambda i,N: 1 + i*(N-1)*N/2
  for i in range(n):
    for N in range(int(round(n/i))+10) if i != 0 else range(n):
      if i > 2 and num(i,N) == n:
        if (N-1) != 11 and (N-1)%10 == 1:
          result.append("{}st {}-gonal number".format(N-1,i))
        elif (N-1) != 12 and (N-1)%10 == 2:
          result.append("{}nd {}-gonal number".format(N-1,i))
        elif (N-1) != 13 and (N-1)%10 == 3:
          result.append("{}rd {}-gonal number".format(N-1,i))
        else:
          result.append("{}th {}-gonal number".format(N-1,i))
  
  return "0th of all" if n == 1 else False if result == [] else result

