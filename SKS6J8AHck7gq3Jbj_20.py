
def tidy_books(lst):
  return [lst[x][0].strip().split(" - ") for x in range(len(lst))]

