
def num_in_str(l):
  return [i for i in l if len(set([type(int(j) if j.isdigit() else j) for j in i])) == 2 or i.isdigit()]

