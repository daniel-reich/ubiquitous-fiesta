
def split_and_delimit(txt, num, delimiter):
  return delimiter.join([txt[x:x+num] for x in range(0,len(txt),num)])

