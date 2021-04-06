
def num_in_str(l):
  new = [i for i in l for j in i if j.isdigit()]
  return sorted(set(new), key=new.index)

