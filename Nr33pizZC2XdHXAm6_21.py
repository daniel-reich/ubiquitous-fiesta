
def months_interval(dateStart, dateEnd):
  months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  m1 = dateStart.strftime("%B")
  m2 = dateEnd.strftime('%B')
  y1 = int(dateStart.strftime("%Y"))
  y2 = int(dateEnd.strftime('%Y'))
  i1 = months.index(m1)
  i2 = months.index(m2)
  if y1 == y2:
    if i1 > i2:
      return months[i2:i1+1]
    elif i1 == i2:
      return [months[i1]]
    else:
      return months[i1:i2+1]
  elif y1 < y2:
    chonk1 = months[i1:]
    chonk2 = months[:i2+1]
    l = chonk1 + chonk2
  else:
    chonk1 = months[i2:]
    chonk2 = months[:i1+1]
  for el in chonk1:
    if el in chonk2:
      chonk2.remove(el)
  l = chonk1 + chonk2
  l1 = []
  for m in months:
    if m in l:
      l1.append(m)
  return l1

