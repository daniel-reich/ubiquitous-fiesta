
def major_sum(lst):
  return max(sum(i for i in lst if i > 0), \
              sum(i for i in lst if i < 0), \
              sum(1 for i in lst if i == 0), key = abs)

