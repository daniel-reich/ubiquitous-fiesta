
def is_prim_pyth_triple(lst):
  a,b,d  = sorted(lst);
  print(a,b,d);
  return a**2 + b**2 == d**2 and are_coprime(a,b,d);
  
def are_coprime(*args):
  all_divs = [div for current in args for div in get_divs(current)];
  return len(all_divs) == len(set(all_divs));
  
def get_divs(number):
  return [k for k in range(2,number) if number%k == 0]

