
def first_and_last(s):
  return (["".join(list(sorted(s)))] + ["".join(list(sorted(s, reverse=True)))])

