
def pile_of_cubes(m):
  counter = 0;
  while m > 0:
    counter+=1;
    m = m - counter**3;
  if m != 0:
    return None;
  else:
    return counter;

