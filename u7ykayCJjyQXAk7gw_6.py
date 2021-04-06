
animals = ["dog", "cat", "bat", "cock", "cow", "pig", 
  "fox", "ant", "bird", "lion", "wolf", "deer", "bear", 
  "frog", "hen", "mole", "duck", "goat"]
  
def contains_animal(animal, txt):
  for i, v in enumerate(animal):
    if txt.find(v) == -1: return False
  return True
  
def remove_animal(animal, txt):
    for i, v in enumerate(animal):
        idx = txt.find(v)
        txt = txt[:idx] + txt[idx+1:]
    return txt
​
def count_animals(txt):
    max = 0
    for i, a in enumerate(animals):
        if contains_animal(a, txt) == False: continue
        cnt = 1 + count_animals(remove_animal(a, txt))
        if cnt > max: max = cnt
    return max

