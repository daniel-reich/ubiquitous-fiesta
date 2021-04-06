
def clean_up_list(lst):
  alist = [int(i) for i in lst if int(i)%2 == 0]
  blist = [int(i) for i in lst if int(i)%2 == 1]
  return [alist,blist]

