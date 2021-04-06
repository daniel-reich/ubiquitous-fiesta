
def sum_two_smallest_nums(lst):
  nlst = [i for i in lst if i > 0]
  return sorted(nlst)[0] + sorted(nlst)[1]

