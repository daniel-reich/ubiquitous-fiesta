
def tune(lst):
  freq, t = [329.63,246.94,196,146.83,110,82.41], []
  for i in range(len(lst)):
    diff = round((lst[i]-freq[i])*100/freq[i])
    if lst[i]==0:
      t.append(' - ')
    elif diff<0:
      if diff<=-3:
        t.append('>>+')
      else:
        t.append('>+')
    elif diff>0:
      if diff>=3:
        t.append('+<<')
      else:
        t.append('+<')
    else:
      t.append('OK')
  return t

