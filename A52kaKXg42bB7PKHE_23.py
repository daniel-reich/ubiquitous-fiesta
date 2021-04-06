
def num_then_char(lst):
  inner_sizes = [len(inner) for inner in lst]
  new_lst = [i for inner in lst for i in inner]
  num_lst = sorted([i for i in new_lst if (type(i) == type(1) or type(i)==type(1.1))])
  char_lst = sorted([i for i in new_lst if type(i) == type('a')])
  lst = num_lst + char_lst
  ans = []
  for size in inner_sizes:
    temp = []
    for i in range(size):
      temp.append(lst.pop(0))
    ans.append(temp)
  return ans

