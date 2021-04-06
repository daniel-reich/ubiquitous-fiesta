
def word_builder(letters, positions):
  result = sorted(zip(letters,positions), key=lambda a: a[1])
  return "".join([i[0] for i in result])

