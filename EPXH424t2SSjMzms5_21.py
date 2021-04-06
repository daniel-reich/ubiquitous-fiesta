
def remix(txt, lst):
  new_arr = []
  for i in range(len(lst)):
    new_arr.append(txt[lst.index(i)])
  return ''.join(new_arr)

