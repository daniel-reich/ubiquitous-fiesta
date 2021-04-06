
def sort_by_last(txt):
  return " ".join(sorted(txt.split(" "), key= lambda word:word[-1:]))

