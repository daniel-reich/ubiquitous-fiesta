
def count_smileys(lst):
  c=0
  for i in lst:
    if len(i)==2:
      if i[0] in ':;' and i[-1] in ')D':
        c += 1
    if len(i)==3:
      if i[0] in ':;' and i[-1] in ')D' and i[1] in '-~':
        c += 1
  return c

