
def leader(lst):
  return [lst[i] for i in range(len(lst)) if all(lst[i]>j for j in lst[i+1:])]

