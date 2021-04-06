
def parity_analysis(num):
  nu = sum([int(i) for i in str(num)])
  return int(num%2) == int(nu%2)

