
def max_separator(txt):
  li = list(set([x for x in [char for char in txt] if [char for char in txt].count(x) > 1]))
  out = []
  length = 0
  for i in li:
    subs = txt[txt.find(i):txt.rfind(i)]
    if max(len(j) for j in subs.split(i)) > length:
      length = max(len(j) for j in subs.split(i))
      out.clear()
      out.append(i)
    elif max(len(j) for j in subs.split(i)) == length:
      out.append(i)
  return sorted(out)

