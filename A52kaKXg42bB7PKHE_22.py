
def num_then_char(lst):
  lst_dict = {}
  num = []
  char = []
  for i in range(len(lst)):
    lst_dict[i] = len(lst[i])
    for j in range(len(lst[i])):
      if str(lst[i][j]).isalpha():
        char.append(lst[i][j])
      else:
        num.append(lst[i][j])
  lst = (sorted(num) + sorted(char))
  ans = []
  v = 0
  for j in lst_dict:
    ans.append(lst[v: lst_dict[j] + v])
    v += lst_dict[j]
  return ans

