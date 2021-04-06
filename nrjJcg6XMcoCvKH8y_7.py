
def validate_subsets(subsets, my_set):
  return all(j in my_set for i in subsets for j in i)

