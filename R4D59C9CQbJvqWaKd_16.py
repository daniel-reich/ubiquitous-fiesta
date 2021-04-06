
def batting_avg(lst):
  a = 0;
  b = 0;
  for L in lst:
    a+= L[0];
    b+= L[1];
  res = str(round(a/b,3))[1:];
  return res if len(res) == 4 else res + "0";

