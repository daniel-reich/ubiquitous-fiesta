
def split_and_delimit(txt, num, delimiter):
  return delimiter.join([txt[c:c+num] for c in range(0,len(txt),num)])

