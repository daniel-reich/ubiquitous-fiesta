
def find_shortest_words(txt):
  all_len= set()
  for i in txt[:-1].split():
    all_len.add(len(i))
  return sorted([i.lower() for i in txt[:-1].split() if len(i)==min(all_len) and i.isalpha()])

