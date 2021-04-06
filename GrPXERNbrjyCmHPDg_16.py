
def duplicate_count(txt):
  foo = set()
  bar = set()
  for i in txt:
    if i in foo:
      bar.add(i)
    else:
      foo.add(i)
  return len(bar)

