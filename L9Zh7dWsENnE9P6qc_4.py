
def josephus(people):
  p=1
  while(p<=people):
    p*=2
  return (2 * people) - p + 1

