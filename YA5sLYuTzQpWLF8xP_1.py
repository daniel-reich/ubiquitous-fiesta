
def clean_up_list(l):
  e = [int(i) for i in l if not int(i)%2]
  o = [int(i) for i in l if int(i) not in e]
  return [e,o]

