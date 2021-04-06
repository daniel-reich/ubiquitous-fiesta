
def pile_of_cubes(m):
  C = 1;
  Tcubes = 0;
  while m>0:
    m-= C**3;
    C+=1;
    if m == 0:
      return C-1;
    elif m - C**3 < 0:
      # ~ #print(C, m,"-------------");
      return None;
​
  return C-1;

