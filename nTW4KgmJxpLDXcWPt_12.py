
def move_to_end(lst, el):
  els = [lst[i] for i in range(len(lst)) if lst[i] == el]
  noels = [lst[i] for i in range(len(lst)) if lst[i] != el]
  return noels + els

