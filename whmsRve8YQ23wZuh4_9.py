
def sort_dates(lst, mode):
#DD-MM-YYYY_HH:MM
  i = 0
  for item in lst:
    dt,tm = item.split("_")
    dd,mm,yy = dt.split("-")
    lst[i] = yy + "-" + mm + "-" + dd + "_" + tm
    i+=1
  if mode=="ASC": 
    lst.sort() 
  else:
    lst.sort(reverse=True)
    
#yyyy-mm-dd_hh:mm
  i=0
  for item in lst:
    dt, tm = item.split("_")
    yy, mm, dd = dt.split("-")
    lst[i] = dd + "-" + mm + "-" + yy + "_" + tm
    i+=1
  
  return lst

