
animals = ["dog", "cat", "bat", "cock", "cow", "pig", 
  "fox", "ant", "bird", "lion", "wolf", "deer", "bear", 
  "frog", "hen", "mole", "duck", "goat"]
  
def count_animals(txt):
  num_animals = 0
  for animal in animals:
    list1 = []
    for i in animal:
      list1.append(txt.count(i))
    if all(list1):
      num_animals += min(list1)
      txt = txt.replace(i,"",min(list1))
  return num_animals

