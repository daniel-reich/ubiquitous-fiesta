
import datetime
from time import strptime
def small_favor(line):
  arr, brr = [], line.split()
  for i in range(len(brr)):
    if '/' in brr[i]:
      validate(brr[i], '/', arr)
    elif '.' in brr[i]:
      validate(brr[i], '.', arr)
    else : 
      arr.append(brr[i])
      try:
        month = strptime(brr[i].replace(",",""), "%B").tm_mon
        if int(brr[brr.index(brr[i])+2][0:2]) < 25:
          brr[brr.index(brr[i])+2] = "20"+brr[brr.index(brr[i])+2]
        else : brr[brr.index(brr[i])+2] = "19"+brr[brr.index(brr[i])+2]
      except : pass
  return " ".join(arr)
​
def validate(x, ch, arr):
  try:
    if int(x.split(ch)[2]) < 25:
      x = x.replace(x.split(ch)[2],"20"+x.split(ch)[2])
      arr.append(datetime.datetime.strptime(x, '%d'+ch+'%m'+ch+'%Y').split()[0])
    else: 
      x = x.replace(x.split(ch)[2],"19"+x.split(ch)[2])
      arr.append(datetime.datetime.strptime(x, '%d'+ch+'%m'+ch+'%Y').split()[0])
  except:
    arr.append(x)

