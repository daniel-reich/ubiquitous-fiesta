
def completely_filled(lst):
  boolean = True
  i = 0
  c = 0
  k = 1
  d = 1
  while i < len(lst):
    while c < len(lst[i]):
      if lst[0][c] != "#":
        boolean = False
      if lst[len(lst) - 1][c] != "#":
        boolean = False
      if lst[i][0] != "#":
        boolean = False
      if lst[i][len(lst[i]) - 1] != "#":
        boolean = False
      
      while k < len(lst) -2:
        while d < len(lst[k]) -1:
          if  lst[k][d] != "*":
            boolean = False
          d+=1
        k+=1
​
      c += 1
    i += 1
    
  if boolean:
    return True
  else:
    return False

