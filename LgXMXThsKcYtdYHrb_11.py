
def split_and_delimit(txt, num, delimiter):
  return delimiter.join(txt[a:a+num] for a in range(0,len(txt),num))

