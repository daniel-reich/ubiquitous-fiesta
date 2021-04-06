
def odd_square_patch(lst):
  lst = [[lst[i][j] % 2 for j in range(0,len(lst[0]))] for i in range(0,len(lst))]
  if not lst:
    return 0
  elif len(lst) == 1:
    return 1 if 1 in lst[0] else 0
  else:
    size = min(len(lst),len(lst[0]))
    while True:
      for i in range(0,len(lst)-size+1):
        for j in range(0,len(lst[0])-size+1):
          if lst[i][j] == 1:
            if all(list(map(lambda x: not 0 in lst[x][j:j+size],range(i,i+size)))):
              return size
      size -= 1

