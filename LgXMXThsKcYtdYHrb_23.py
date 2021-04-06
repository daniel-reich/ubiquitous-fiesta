
def split_and_delimit(txt, num, delimiter):
  return delimiter.join(txt[i:i + num] for i in range(0,len(txt),num))

