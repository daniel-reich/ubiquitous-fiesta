
def bed_time(*times):
  out = []
  for i in times:
    h = int(i[0][:2]) - int(i[1][:2])
    m = int(i[0][-2:]) - int(i[1][-2:])
    if m < 0:
      m = str(m + 60)
      h -= 1
    elif m < 10:
      m = '0' + str(m)
    else: m = str(m)
    if h < 0:
      h = str(h + 24)
    elif h < 10:
      h = '0' + str(h)
    else: h = str(h)
    
    time = h + ':' + m
    out.append(time)
    
  return out

