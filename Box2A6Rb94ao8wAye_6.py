
def leader(lst):
  return [lst[i] for i in range(len(lst)) if lst[i] == max(lst[i:])]

