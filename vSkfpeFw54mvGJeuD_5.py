
def lychrel(n):
  number = str(n);
  if list(number) == list(number[::-1]):
    return 0;
  temp = n;
  for i in range(500):
    number = str(n);
    if list(number) == list(number[::-1]):
      return i;
    n = n + int(number[::-1]);
  return True;

