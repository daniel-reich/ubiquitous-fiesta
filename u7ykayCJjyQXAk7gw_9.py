
import math
animals = ["dog", "cat", "bat", "cock", "cow", "pig", 
  "fox", "ant", "bird", "lion", "wolf", "deer", "bear", 
  "frog", "hen", "mole", "duck", "goat"]
​
def chars(txt):
  tmp=[0]*256
  for i in txt:
    tmp[ord(i)] += 1
  return tmp
​
​
​
def count_animals2(txt):
  data=chars(txt)
  counting=0
  print(txt)
​
  for a in animals:
    tmp=chars(a)
    max=99999
    for d,t in zip(data,tmp):
      if t>0:
        max=min(max,math.floor(d/t))
    if max>0:
      print(max,a)
    counting += max
    for count,t in enumerate(tmp):
      data[count] -= t*max
  for i,a in enumerate(data):
    if a>0:
      print(a,chr(i))
  
  return counting
  
def count_animals(txt):
  tmp=count_animals2(txt)
  animals.reverse()
  tmp=max(tmp,count_animals2(txt) )
  return tmp

