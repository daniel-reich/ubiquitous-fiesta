
def get_languages(num):
​
  from itertools import combinations as c
​
  languages = {'C#': 1, 'C++': 2, 'Java': 4, 'JavaScript': 8, 'PHP': 16, 'Python': 32, 'Ruby': 64, 'Swift': 128}
​
  if num in languages.values():
    for key in languages.keys():
      v = languages[key]
      if v == num:
        return [key]
      
  points = list(languages.values())
​
  combins = []
​
  for n in range(2, 9):
    combins.append(list(c(points, n)))
  
  valid_combins = []
​
  for combinations in combins:
    for combination in combinations:
      s = sum(list(combination))
      if s == num:
        for n in combination:
          valid_combins.append(n)
  
  
  known = []
​
  for key in languages.keys():
    val = languages[key]
    if val in valid_combins:
      known.append(key)
  
  order = 'C# C++ Java JavaScript PHP Python Ruby Swift'.split()
​
  knownordered = []
​
  for lang in order:
    if lang in known:
      knownordered.append(lang)
  
  return knownordered

