
def check(lst):
  return "YES" if lst != sorted(lst) and str(sorted(lst))[1:-1] in str(lst * 2) else "NO"

