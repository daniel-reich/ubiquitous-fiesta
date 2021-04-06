
A = ["dog", "cat", "bat", "cock", "cow", "pig", 
  "fox", "ant", "bird", "lion", "wolf", "deer", "bear", 
  "frog", "hen", "mole", "duck", "goat"]
​
​
def count_animals(txt):
  c, txt = 0, list(txt)
​
  for animal in A:
    while all(l in txt for l in animal):
      c += 1
      [txt.pop(txt.index(l)) for l in animal]
        
  return c + (0, 1)['w' in txt]

