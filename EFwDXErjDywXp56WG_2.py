
def is_in_order(txt):
  return all([txt[i] <= txt[i + 1] for i in range(len(txt) - 1)])

