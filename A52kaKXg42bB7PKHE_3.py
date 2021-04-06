
def num_then_char(lst):
  sort = sorted(j for i in lst for j in i if type(j)!=str)  + sorted(j for i in lst for j in i if type(j)==str)
  ans = []
  for i in map(len, lst):
    new_lst = [sort.pop(0) for j in range(i)]
    ans.append(new_lst)
  return ans

