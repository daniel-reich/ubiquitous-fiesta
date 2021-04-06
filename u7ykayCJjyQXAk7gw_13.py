
animals = ["dog", "cat", "bat", "cock", "cow", "pig", 
  "fox", "ant", "bird", "lion", "wolf", "deer", "bear", 
  "frog", "hen", "mole", "duck", "goat"]
​
def count_animals(txt,c=0):
  if any([all([txt.count(i)>=j.count(i) for i in j]) for j in animals]):
    return max([count_animals(remove(txt,i),c+1) for i in animals if all([txt.count(j)>=i.count(j) for j in i])])
  else:
    return c
    
def remove(txt,a):
  for i in a:
    txt=txt[:txt.index(i)]+txt[txt.index(i)+1:]
  return txt

