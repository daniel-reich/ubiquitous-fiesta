
def is_correct_aliases(names, aliases):
  return all(all(i[0]==k[0] for i in v.split()) for k, v in zip(names, aliases))

