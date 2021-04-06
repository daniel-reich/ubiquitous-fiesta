
def clean_up_list(lst):
  e = [int(i) for i in lst if int(i)%2==0]
  o = [int(i) for i in lst if int(i)%2==1]
  return [e, o]

