
def histogram(lst, char):
  return char*lst[0] + ''.join(['\n'+char*i for i in lst[1:]])

