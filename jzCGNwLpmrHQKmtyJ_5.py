
def parity_analysis(n):
  return sum(int(i) for i in str(n)) % 2 == n % 2

