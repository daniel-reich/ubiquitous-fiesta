
def distance_to_nearest_vowel(x):
  vowels=['a','e','i','o','u']
  positions=[]
  for element in range(len(x)):
    if x[element] in vowels:
      positions.append(element)
  final=[]
  for element1 in range(len(x)):
    if x[element1] in vowels:
      final.append(0)
    if x[element1] not in vowels:
      minimum=len(x)
      for element2 in positions:
        if element1-element2<0:
          y=-(element1-element2)
          if y<minimum:
            minimum=y
        if element1-element2>0:
          y=(element1-element2)
          if y<minimum:
            minimum=y
      final.append(minimum)
  return final

