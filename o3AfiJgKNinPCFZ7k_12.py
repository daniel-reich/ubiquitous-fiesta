
def partition(txt, n):
  holder = []
  for i in range(0, len(txt), n):
    holder.append(txt[i: i + n])
  return holder

