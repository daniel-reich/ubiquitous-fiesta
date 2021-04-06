
def delete_occurrences(lst, num):
  return [i for idx, i in enumerate(lst) if lst[:idx+1].count(i) <= num]

