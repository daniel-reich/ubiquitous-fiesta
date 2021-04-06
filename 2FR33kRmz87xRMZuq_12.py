
def histogram(lst, char):
  updated_lst = []
  for i in lst:
    updated_lst.append(char * i)
  return '\n'.join(updated_lst)

