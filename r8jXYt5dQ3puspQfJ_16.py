
def split(txt):
  beg = []
  end = []
  for i in txt:
    if i in 'aeiou':
      beg.append(i)
    else:
      end.append(i)
  return ''.join(beg) + ''.join(end)

