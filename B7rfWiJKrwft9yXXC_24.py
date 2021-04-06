
def sort_decending(num):
  sol = [int(i) for i in str(num)]
  sol = sorted(sol, reverse = True)
  sol = [str(i) for i in sol]
  sol = "".join(sol)
  return int(sol)

