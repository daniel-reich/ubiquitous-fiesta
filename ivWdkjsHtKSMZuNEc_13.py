
def find_shortest_words(txt):
  lst = sorted(txt.rstrip(".").lower().split(), key = len)
  lst1 = [lst[i] for i in range(len(lst)) if len(lst[i]) == len(lst[0]) and lst[i].isalpha()]
  return sorted(lst1)

