
def histogram(lst, char):
  return ''.join([char*lst[i]+'\n' if i != len(lst)-1 else char*lst[i] for i in range(0,len(lst))])

