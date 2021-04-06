
def switches(n):
  bin_sol = ("10"*n)[:n]  #solution as a binary number
  return sum(int(bin_sol[::-1][i])*2**i for i in range(len(bin_sol)))

