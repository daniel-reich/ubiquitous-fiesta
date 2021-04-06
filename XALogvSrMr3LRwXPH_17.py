
def is_shuffled_well(lst):
  cnt = 0
  for i in range(len(lst) - 2):
    if lst[i] == lst[i + 1] - 1 and lst[i] == lst[i + 2] - 2 or lst[i] == lst[i + 1] + 1 and lst[i] == lst[i + 2] + 2:
      cnt += 1
  return cnt == 0

