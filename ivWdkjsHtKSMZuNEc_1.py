
def find_shortest_words(txt):
  return sorted([x.lower() for x in txt.replace(".", "").split(' ') if len(x) == min([len(x) for x in txt.split(' ')]) and x.isalpha()])

