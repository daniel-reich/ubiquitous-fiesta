
def sort_by_last(txt):
  listed = txt.split(' ')
  i = 0
  final = []
  while len(listed) > 0:
    alphabetical = listed[0][-1]
    alphindex = i
    while i < len(listed):
      if listed[i][-1] < alphabetical:
        alphabetical = listed[i][-1]
        alphindex = i
      i += 1
    final.append(listed[alphindex])
    listed.pop(alphindex)
    i = 0
  result = ' '.join(final)
  return(result)

