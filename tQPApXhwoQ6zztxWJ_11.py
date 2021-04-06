
def get_prices(lst):
  ans = []
  for ele in lst:
    txt = ele.split()
    ans.append(float(txt[-1].strip("$()")))
  return ans

