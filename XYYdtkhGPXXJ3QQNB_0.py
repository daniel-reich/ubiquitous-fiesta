
def num_in_str(lst):
  return [i for i in lst if any(j.isdigit() for j in i)]

