
def months_interval(dateStart, dateEnd):
  m=['January','February','March','April','May','June','July',
  'August','September','October','November','December']
  start=str(dateStart).split('-')
  end=str(dateEnd).split('-')
  if start[0]==end[0]:
    if start[1]==end[1]: return [m[int(start[1])-1]]
    else: 
      if int(start[1])>int(end[1]): start,end=end,start
      return m[int(start[1])-1:int(end[1])]
  elif abs(int(start[0])-int(end[0]))>1: return m
  else:
    if int(start[0])>int(end[0]): start,end=end,start
    ans=m[int(start[1])-1:]
    ans2=m[:int(end[1])]
    for i in ans2:
      if i not in ans: ans.append(i)
    return [i for i in m if i in ans]

