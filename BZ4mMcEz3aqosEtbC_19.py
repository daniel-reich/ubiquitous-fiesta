
def mean(num):
  num_list = []
  for x in str(num):
    num_list.append(int(x))
  return sum(num_list) / len(num_list)

