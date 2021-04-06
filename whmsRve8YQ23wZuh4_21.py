
import datetime
from datetime import datetime
def sort_dates(lst, mode):
  dateStrList=[]
  for i in lst:
    dateFormattedStr = datetime.strftime(datetime.strptime(i,'%d-%m-%Y_%H:%M'),'%Y-%m-%d %H:%M')
    dateStrList.append(dateFormattedStr)
  if mode.upper()=="ASC":
    dateStrList=sorted(dateStrList)
  else:
    dateStrList=sorted(dateStrList,reverse=True)
  for i in range(len(dateStrList)):
    dateStrList[i] = datetime.strftime(datetime.strptime(dateStrList[i],'%Y-%m-%d %H:%M'),'%d-%m-%Y_%H:%M')
  return dateStrList

