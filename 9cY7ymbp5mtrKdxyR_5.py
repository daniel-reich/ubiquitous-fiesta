
from math import ceil,floor
def encryption(txt):
  new=""
  for i in txt:
    if i!=" ":
      new+=i
  l=ceil(len(new)**0.5)
  rows=[]
  for i in range(ceil(len(new)/l)):
    rows.append((new[i*l:(i+1)*l]))
  end=""
  for i in range(l):
    for j in rows:
      if len(j)>i:
        end+=j[i]
    end+=" "
  return end[0:-1]

