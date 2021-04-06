
def one_odd_one_even(n):
  return sorted(int(i)%2 for i in str(n)) == [0,1]

