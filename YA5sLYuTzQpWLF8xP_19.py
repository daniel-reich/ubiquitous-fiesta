
def clean_up_list(x):
  return [[int(i) for i in x if not int(i)%2], [int(i) for i in x if int(i)%2]]

