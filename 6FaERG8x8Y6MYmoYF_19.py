
def dice_score(throw):
  d = {'111' : 1000,
    '222' : 200,
    '333' : 300,
    '444' : 400,
    '555' : 500,
    '666' : 600,
    '1' : 100,
    '5' : 50}
  st = ''.join(sorted(map(str, throw)))
  count = 0
  for i in sorted(d, key=len, reverse=True):
    if i in st:
      count += d[i]
      st = st.replace(i, '')
  return count

