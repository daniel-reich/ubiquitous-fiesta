
def sort_dates(lst, mode):
  descending = True
  if mode != "DSC":
    descending = False 
  lst.sort(key = lambda x: (year(x), month(x), day(x), hour(x), minute(x)), reverse = descending)
  return lst
  
def year(date):
  return date[6:10]
  
def month(date):
  return date[3:5]
​
def day(date):
  return date[:2]
​
def hour(date):
  return date[11:13]
​
def minute(date):
  return date[14:]

