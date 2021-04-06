
def josephus(n):
  if n < 1:
    return False
  else:
    clst =  [1] * n
    i = 0
    while sum(clst) != 1:
      if clst[i] == 1:
        for j in range(n):
          i_j = (i + j + 1) % n
          if clst[i_j] == 1:
            clst[i_j] = 0
            break
      if sum(clst) ==1:
        break
      else:
        i += 1
        i = i % n
  return i

