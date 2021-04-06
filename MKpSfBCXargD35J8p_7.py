
def journey_distance(n):
  if n < 3:
    return 0;
  elif n == 3:
    return 1;
  else:
    res = 1;
    res += (n - 3) / 2;
    return res;

