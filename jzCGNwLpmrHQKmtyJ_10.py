
def parity_analysis(num):
  ls = list(map(int, str(num)))
  return (sum(ls) % 2 == 0 and num % 2 == 0) or (sum(ls) % 2 != 0 and num % 2 != 0)

